#!/bin/bash
BASE="$(cd "$(dirname "$0")" && pwd)"
RAW="$BASE/_raw"; mkdir -p "$RAW"
ok=0; falta=0
while IFS=$'\t' read -r bloco ad formato ident; do
  [ "$bloco" = "bloco" ] && continue
  url=$(awk -F'\t' -v id="$ident" '$1==id{print $2; exit}' "$BASE/_urls.tsv")
  if [ -z "$url" ]; then falta=$((falta+1)); continue; fi
  out="$RAW/${bloco}-ad${ad}-${formato}.png"
  if [ ! -s "$out" ]; then curl -sS -o "$out" "$url"; fi
  [ -s "$out" ] && ok=$((ok+1))
done < "$BASE/_registro-geracao.tsv"
echo "baixados: $ok · sem url ainda: $falta"
