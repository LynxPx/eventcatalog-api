#!/bin/bash
term_width=$(tput cols)
msg="Starting API Python venv..."
padding=$(( (term_width - ${#message}) / 2 -10))

echo ""
line=$(printf '%*s' "$term_width" | tr ' ' '#')
echo "$line"
printf "%*s\n" $((padding + ${#msg})) "$msg"
echo "$line"
echo ""


source /Users/kulylanellc/Library/Caches/pypoetry/virtualenvs/eventcatalog-api-36bAStYg-py3.12/bin/activate
#cd fastapi/
poetry run uvicorn server:app --reload
# New way for final structure
#poetry run uvicorn eventcatalog_api.server:app --reload

closing_msg="Stopping API Server & Deactivating env..."
echo ""
line=$(printf '%*s' "$term_width" | tr ' ' '#')
echo "$line"
printf "%*s\n" $((padding + ${#closing_msg})) "$closing_msg"
echo "$line"
echo ""
# Exit venv
deactivate