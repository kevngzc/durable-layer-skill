#!/usr/bin/env bash
# Package the skill for claude.ai / Claude Desktop upload → dist/durable-layer.skill (zip, one top-level folder).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/durable-layer.skill
zip -qr dist/durable-layer.skill durable-layer -x '*/__pycache__/*' '*.pyc' '*/.DS_Store'
unzip -l dist/durable-layer.skill | tail -n +4 | sed '$d' | sed '$d'
echo "→ dist/durable-layer.skill"
