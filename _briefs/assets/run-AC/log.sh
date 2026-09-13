#!/bin/zsh
# usage: log.sh "done: ... next: ..."
MK="/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit"
echo "- $(date '+%Y-%m-%d %H:%M') $1" >> "$MK/_BUILD-LOG/TERMINAL-B-live.md"
