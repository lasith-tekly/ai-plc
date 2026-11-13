#!/usr/bin/env python3
"""Refresh the Claude Code marketplace entry in this repository.

Builds the packages into a temporary folder, copies the Claude Code plugin to
plugins/ai-plc, and writes .claude-plugin/marketplace.json. Run it after any
change to the source, then commit plugins/ and .claude-plugin/.

    python3 tools/sync_marketplace.py
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_DIR = ROOT / "plugins" / "ai-plc"


def main():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "dist"
        subprocess.run([sys.executable, str(ROOT / "build" / "build_packages.py"), str(out)], check=True)
        built = out / "claude-code-plugin" / "ai-plc"
        if PLUGIN_DIR.exists():
            shutil.rmtree(PLUGIN_DIR)
        PLUGIN_DIR.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(built, PLUGIN_DIR)

    manifest = json.loads((PLUGIN_DIR / ".claude-plugin" / "plugin.json").read_text())
    market = {
        "name": "ai-plc",
        "description": "AI-PLC: an open-source agent harness for product ideation and planning, led by the PM.",
        "owner": {"name": "Lasith Jayarathne"},
        "plugins": [
            {
                "name": manifest["name"],
                "source": "./plugins/ai-plc",
                "description": manifest["description"],
                "version": manifest["version"],
            }
        ],
    }
    dest = ROOT / ".claude-plugin" / "marketplace.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(market, indent=2) + "\n")
    print("marketplace updated:", manifest["name"], manifest["version"])


if __name__ == "__main__":
    main()
