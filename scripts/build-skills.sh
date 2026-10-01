#!/usr/bin/env bash
# Copy the shared files into every skill (so each skill is self-contained)
# and package each one as dist/<skill>.zip for upload to claude.ai.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for dir in skills/*/; do
  name=$(basename "$dir")
  mkdir -p "$dir/scripts" "$dir/references"
  cp shared/colour_tools.py "$dir/scripts/colour_tools.py"
  cp shared/applying-in-tools.md "$dir/references/applying-in-tools.md"
  (cd skills && zip -qr "../dist/$name.zip" "$name" -x '*/__pycache__/*')
  echo "packaged dist/$name.zip"
done
