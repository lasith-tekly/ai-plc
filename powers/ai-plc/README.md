# AI-PLC Setup (Kiro power)

A small Kiro power that installs the full AI-PLC package into a project when you ask Kiro to set it up. It runs the repository's `install.sh` (Mac and Linux) or `install.ps1` (Windows), previews first, and asks for approval before copying anything. It never overwrites existing files.

It does not contain the AI-PLC agents itself. A Kiro power can hold skills and connections but not custom agents, and AI-PLC needs its separate reviewer agent.

Import it in Kiro: Powers panel, **Add Custom Power**, **Import power from GitHub**, then
`https://github.com/lasith-tekly/ai-plc/tree/main/powers/ai-plc`

Docs: https://lasith-tekly.github.io/ai-plc/ . Licence: Apache 2.0.
