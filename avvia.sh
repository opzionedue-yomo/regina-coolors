#!/bin/zsh
# Accende il sito Regina Coolors in locale sulla porta 8910.
cd "$(dirname "$0")/sito" || exit 1
echo "▶︎  Regina Coolors — http://localhost:8910   (Ctrl+C per spegnere)"
python3 -m http.server 8910
