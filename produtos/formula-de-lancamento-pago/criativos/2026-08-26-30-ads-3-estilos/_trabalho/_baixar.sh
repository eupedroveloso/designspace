#!/bin/bash
B="$(cd "$(dirname "$0")" && pwd)"; R="$B/_lote20"; mkdir -p "$R"; ok=0; falta=0
while IFS=$'\t' read -r n ident; do
  url=$(awk -F'\t' -v id="$ident" '$1==id{print $2; exit}' "$B/_u20.tsv")
  [ -z "$url" ] && { falta=$((falta+1)); continue; }
  out="$R/ad$n.png"; [ ! -s "$out" ] && curl -sS -o "$out" "$url"
  [ -s "$out" ] && ok=$((ok+1))
done < "$B/_reg20.tsv"
echo "baixados: $ok · faltam: $falta"
