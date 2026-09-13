#!/usr/bin/env bash
# Fetch every external SVG the README renders into assets/, so the page does
# not depend on anyone else's hosting staying up.
# A failed fetch NEVER clobbers the good vendored copy already in the repo.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE/.." || exit 1
rc=0
while IFS=$'\t' read -r dest url; do
  case "$dest" in ''|\#*) continue;; esac
  tmp=$(mktemp)
  if curl -sf --max-time 30 "$url" -o "$tmp" && head -c 400 "$tmp" | grep -q '<svg'; then
    mv "$tmp" "$dest"; echo "ok    $dest"
  else
    rm -f "$tmp"; echo "STALE $dest - source unreachable, keeping vendored copy"; rc=1
  fi
done < "$HERE/vendor-urls.txt"
exit $rc
