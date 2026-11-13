# AI-PLC installer for Windows (PowerShell). Copies the AI-PLC files for one tool
# into a project folder. It matches install.sh.
#
# Usage, from your project folder in PowerShell:
#   & ([scriptblock]::Create((irm https://raw.githubusercontent.com/lasith-tekly/ai-plc/main/install.ps1))) kiro
#
# Tools: kiro | claude-code | codex | copilot
# Options: -Dir PATH  -Version TAG  -Zip FILE  -DryRun  -Force
#
# It downloads ai-plc-packages.zip from the newest GitHub release and never
# overwrites a file that already exists, unless you add -Force. Read this file
# first if you prefer; it is short.

param(
    [Parameter(Position = 0)][string]$Tool = "",
    [string]$Dir = ".",
    [string]$Version = "",
    [string]$Zip = "",
    [switch]$DryRun,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$Repo = "lasith-tekly/ai-plc"
$FallbackTag = "v1.0.0-rc2"

function Show-Usage {
    Write-Host "Usage: install.ps1 <tool> [-Dir PATH] [-Version TAG] [-Zip FILE] [-DryRun] [-Force]"
    Write-Host ""
    Write-Host "Tools:"
    Write-Host "  kiro          Kiro (.kiro)"
    Write-Host "  claude-code   Claude Code, drop-in folder (.claude and .mcp.json)"
    Write-Host "  codex         Codex (.codex and .agents)"
    Write-Host "  copilot       GitHub Copilot, experimental (.github and .vscode)"
}

$work = $null
try {
    $items = switch ($Tool) {
        "kiro"        { "kiro/.kiro|.kiro" }
        "claude-code" { "claude-code-project/.claude|.claude", "claude-code-project/.mcp.json|.mcp.json" }
        "codex"       { "codex/.codex|.codex", "codex/.agents|.agents" }
        "copilot"     { "copilot/.github|.github", "copilot/.vscode|.vscode" }
        default       { $null }
    }
    if (-not $items) {
        Show-Usage
        throw "choose a tool: kiro, claude-code, codex or copilot"
    }
    if (-not (Test-Path -LiteralPath $Dir -PathType Container)) { throw "folder not found: $Dir" }
    $destRoot = (Resolve-Path -LiteralPath $Dir).Path

    $work = Join-Path ([System.IO.Path]::GetTempPath()) ("aiplc-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $work | Out-Null

    if ($Zip -eq "") {
        # Older Windows PowerShell needs TLS 1.2 switched on for GitHub.
        try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch { }
        if ($Version -eq "") {
            try {
                # The newest release, including release candidates.
                $rel = Invoke-RestMethod -UseBasicParsing -Uri "https://api.github.com/repos/$Repo/releases?per_page=1"
                $Version = @($rel)[0].tag_name
            } catch { $Version = "" }
            if (-not $Version) { $Version = $FallbackTag }
        }
        $url = "https://github.com/$Repo/releases/download/$Version/ai-plc-packages.zip"
        Write-Host "Downloading AI-PLC $Version ..."
        $zipPath = Join-Path $work "pkg.zip"
        try { Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $zipPath } catch { throw "download failed: $url" }
    } else {
        if (-not (Test-Path -LiteralPath $Zip -PathType Leaf)) { throw "zip not found: $Zip" }
        $zipPath = (Resolve-Path -LiteralPath $Zip).Path
    }

    $extract = Join-Path $work "x"
    Expand-Archive -LiteralPath $zipPath -DestinationPath $extract -Force

    if ($DryRun) { Write-Host "Dry run: nothing will be changed." }
    Write-Host "Installing the $Tool package into $destRoot"

    # A hashtable, so the counters work from inside the function in any run mode.
    $stats = @{ copied = 0; skipped = 0 }

    function Copy-One([string]$from, [string]$to, [string]$shown) {
        if ((Test-Path -LiteralPath $to) -and (-not $Force)) {
            $stats.skipped++
            Write-Host "  kept (already exists): $shown"
            return
        }
        $stats.copied++
        if ($DryRun) {
            Write-Host "  would copy: $shown"
        } else {
            $parent = Split-Path -Parent $to
            if (-not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
            Copy-Item -LiteralPath $from -Destination $to -Force
        }
    }

    foreach ($pair in @($items)) {
        $parts = $pair.Split("|")
        $srcRel = $parts[0]
        $name = $parts[1]
        $src = Join-Path $extract ($srcRel -replace "/", "\")
        if (-not (Test-Path -LiteralPath $src)) { throw "this release does not contain $srcRel" }
        if (Test-Path -LiteralPath $src -PathType Container) {
            $srcFull = (Resolve-Path -LiteralPath $src).Path.TrimEnd("\")
            Get-ChildItem -LiteralPath $src -Recurse -File -Force | ForEach-Object {
                $rel = $_.FullName.Substring($srcFull.Length).TrimStart("\")
                Copy-One $_.FullName (Join-Path (Join-Path $destRoot $name) $rel) (Join-Path $name $rel)
            }
        } else {
            Copy-One $src (Join-Path $destRoot $name) $name
        }
    }

    Write-Host ""
    if ($DryRun) {
        Write-Host "Dry run done: $($stats.copied) file(s) would be copied, $($stats.skipped) kept."
    } else {
        Write-Host "Done: $($stats.copied) file(s) copied, $($stats.skipped) kept."
    }
    if ($stats.skipped -gt 0 -and (-not $Force)) {
        Write-Host "Files that already existed were not changed. If one is a connection file"
        Write-Host "(.mcp.json, mcp.json, config.toml), add the AI-PLC entries by hand. See MCP-SETUP.md."
    }
    Write-Host ""
    Write-Host "Next: open the project in your tool and run:  /ai-plc --ideation `"<your idea>`""
    Write-Host "Try it on a test idea first. Do not use confidential material."
}
catch {
    Write-Host ("Error: " + $_.Exception.Message) -ForegroundColor Red
}
finally {
    if ($work -and (Test-Path -LiteralPath $work)) { Remove-Item -LiteralPath $work -Recurse -Force -ErrorAction SilentlyContinue }
}
