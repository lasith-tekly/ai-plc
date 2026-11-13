#!/bin/sh
# AI-PLC installer. Copies the AI-PLC files for one tool into a project folder.
#
# Usage:
#   sh install.sh <tool> [--dir PATH] [--version TAG] [--zip FILE] [--dry-run] [--force]
#
# Tools: kiro | claude-code | codex | copilot
#
# By default it downloads ai-plc-packages.zip from the newest GitHub release,
# and never overwrites a file that already exists. Use --dry-run to see what
# would be copied. Read this file first if you prefer; it is short.

set -eu

REPO="lasith-tekly/ai-plc"
FALLBACK_TAG="v1.0.0-rc2"

TOOL=""
DIR="."
TAG=""
ZIP=""
DRY=0
FORCE=0

say() { printf '%s\n' "$*"; }
die() { printf 'Error: %s\n' "$*" >&2; exit 1; }

usage() {
  cat <<'EOF'
Usage: sh install.sh <tool> [options]

Tools:
  kiro          Kiro (.kiro)
  claude-code   Claude Code, drop-in folder (.claude and .mcp.json)
  codex         Codex (.codex and .agents)
  copilot       GitHub Copilot, experimental (.github and .vscode)

Options:
  --dir PATH     Project folder to install into (default: current folder)
  --version TAG  Release tag to install (default: newest release)
  --zip FILE     Use a local ai-plc-packages.zip instead of downloading
  --dry-run      Show what would be copied, change nothing
  --force        Overwrite files that already exist
  -h, --help     Show this help

Claude Code can also install AI-PLC as a plugin. See the README.
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    kiro|claude-code|codex|copilot) TOOL="$1" ;;
    --dir) [ $# -ge 2 ] || die "--dir needs a path"; DIR="$2"; shift ;;
    --version) [ $# -ge 2 ] || die "--version needs a tag"; TAG="$2"; shift ;;
    --zip) [ $# -ge 2 ] || die "--zip needs a file"; ZIP="$2"; shift ;;
    --dry-run) DRY=1 ;;
    --force) FORCE=1 ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; die "unknown argument: $1" ;;
  esac
  shift
done

[ -n "$TOOL" ] || { usage >&2; die "choose a tool: kiro, claude-code, codex or copilot"; }
[ -d "$DIR" ] || die "folder not found: $DIR"

# What to copy, as "folder-in-zip:name-in-project" pairs.
case "$TOOL" in
  kiro)        ITEMS="kiro/.kiro:.kiro" ;;
  claude-code) ITEMS="claude-code-project/.claude:.claude claude-code-project/.mcp.json:.mcp.json" ;;
  codex)       ITEMS="codex/.codex:.codex codex/.agents:.agents" ;;
  copilot)     ITEMS="copilot/.github:.github copilot/.vscode:.vscode" ;;
esac

WORK="$(mktemp -d 2>/dev/null || mktemp -d -t aiplc)"
trap 'rm -rf "$WORK"' EXIT INT TERM

if [ -z "$ZIP" ]; then
  command -v curl >/dev/null 2>&1 || die "curl is needed to download the release (or pass --zip FILE)"
  if [ -z "$TAG" ]; then
    # The newest release, including release candidates.
    TAG="$(curl -fsSL "https://api.github.com/repos/$REPO/releases?per_page=1" 2>/dev/null \
      | sed -n 's/.*"tag_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1 || true)"
    [ -n "$TAG" ] || TAG="$FALLBACK_TAG"
  fi
  URL="https://github.com/$REPO/releases/download/$TAG/ai-plc-packages.zip"
  say "Downloading AI-PLC $TAG ..."
  curl -fsSL "$URL" -o "$WORK/pkg.zip" || die "download failed: $URL"
  ZIP="$WORK/pkg.zip"
else
  [ -f "$ZIP" ] || die "zip not found: $ZIP"
fi

mkdir -p "$WORK/x"
if command -v unzip >/dev/null 2>&1; then
  unzip -q "$ZIP" -d "$WORK/x"
elif command -v python3 >/dev/null 2>&1; then
  python3 -c 'import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])' "$ZIP" "$WORK/x"
else
  die "unzip or python3 is needed to open the package"
fi

COPIED=0
SKIPPED=0

copy_one() {  # $1 = source path, $2 = destination path
  if [ -e "$2" ] && [ "$FORCE" -ne 1 ]; then
    SKIPPED=$((SKIPPED + 1))
    say "  kept (already exists): ${2#"$DIR"/}"
    return 0
  fi
  COPIED=$((COPIED + 1))
  if [ "$DRY" -eq 1 ]; then
    say "  would copy: ${2#"$DIR"/}"
  else
    mkdir -p "$(dirname "$2")"
    cp "$1" "$2"
  fi
}

[ "$DRY" -eq 1 ] && say "Dry run: nothing will be changed."
say "Installing the $TOOL package into $DIR"

for pair in $ITEMS; do
  SRC="$WORK/x/${pair%%:*}"
  NAME="${pair#*:}"
  [ -e "$SRC" ] || die "this release does not contain ${pair%%:*}"
  if [ -d "$SRC" ]; then
    ( cd "$SRC" && find . -type f ) | while IFS= read -r f; do
      printf '%s\n' "$f"
    done > "$WORK/list"
    while IFS= read -r f; do
      copy_one "$SRC/$f" "$DIR/$NAME/${f#./}"
    done < "$WORK/list"
  else
    copy_one "$SRC" "$DIR/$NAME"
  fi
done

say ""
if [ "$DRY" -eq 1 ]; then
  say "Dry run done: $COPIED file(s) would be copied, $SKIPPED kept."
else
  say "Done: $COPIED file(s) copied, $SKIPPED kept."
fi
if [ "$SKIPPED" -gt 0 ] && [ "$FORCE" -ne 1 ]; then
  say "Files that already existed were not changed. If one is a connection file"
  say "(.mcp.json, mcp.json, config.toml), add the AI-PLC entries by hand. See MCP-SETUP.md."
fi
say ""
say "Next: open the project in your tool and run:  /ai-plc --ideation \"<your idea>\""
say "Try it on a test idea first. Do not use confidential material."
