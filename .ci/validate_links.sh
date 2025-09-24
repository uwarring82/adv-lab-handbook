#!/usr/bin/env bash
set -euo pipefail
FAILS=0
while read -r url; do
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" -m 10 -L "$url" 2>/dev/null) || STATUS="000"
  if [[ ! $STATUS =~ ^(2|3)[0-9]{2}$ ]]; then
    echo "Broken or slow link: $url (status: $STATUS)"; FAILS=$((FAILS+1))
  fi
done < <(grep -RhoE "https?://[a-zA-Z0-9./_%-]+" handbook | sort -u)
if [ $FAILS -gt 0 ]; then
  echo "Found $FAILS problematic links."; exit 1; fi
