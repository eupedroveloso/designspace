#!/usr/bin/env bash
#
# Destino no Figma — trava e registro.
#
# O projeto não cria nada no Figma sem que o usuário tenha dito, nesta sessão,
# em qual arquivo a peça deve nascer. Este script é quem faz a regra valer.
#
#   guard   chamado pelo hook PreToolUse — bloqueia escrita no Figma sem destino
#   set     registra o destino a partir do link que o usuário deu
#   show    imprime o destino ativo
#   clear   apaga o registro — chamado pelo hook SessionStart
#
# O registro vive em .claude/state/figma-destino.json, fora do versionamento,
# e morre a cada sessão nova. Sessão nova, pergunta nova.

set -uo pipefail

RAIZ="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
ESTADO="$RAIZ/.claude/state/figma-destino.json"

escapa() { printf '%s' "${1:-}" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g'; }

# ---------------------------------------------------------------- guard

guard() {
  [ -s "$ESTADO" ] && exit 0

  cat >&2 <<'FIM'
DESTINO NO FIGMA NÃO REGISTRADO — pare aqui, não crie nada.

Nenhum arquivo de destino foi confirmado pelo usuário nesta sessão. Antes de
qualquer criação ou edição no Figma:

  1. PERGUNTE ao usuário o link do arquivo Figma onde a peça deve ser criada.
     Pergunte junto a página e a seção, se ele souber.
  2. REGISTRE a resposta dele:

     .claude/hooks/figma-destino.sh set "<link>" --pagina "<página>" --secao "<seção>"

  3. Repita então esta chamada.

Não escolha o arquivo por conta própria. Link de sessão anterior, de memória,
do CLAUDE.md ou de um output antigo não vale como resposta — o usuário precisa
dizer agora, nesta conversa. Se ele quiser um arquivo novo, ele decide o nome e
onde; registre o link depois de criado.

Detalhes do ritual em .claude/skills/figma-destino/SKILL.md (/figma-destino).
FIM
  exit 2
}

# ---------------------------------------------------------------- set

registrar() {
  local url="${1:-}" pagina="" secao="" nota=""
  [ -n "$url" ] || { echo "uso: figma-destino.sh set \"<link do Figma>\" [--pagina X] [--secao Y] [--nota Z]" >&2; exit 1; }
  shift

  while [ $# -gt 0 ]; do
    case "$1" in
      --pagina) pagina="${2:-}"; shift 2 ;;
      --secao)  secao="${2:-}";  shift 2 ;;
      --nota)   nota="${2:-}";   shift 2 ;;
      *) echo "argumento desconhecido: $1" >&2; exit 1 ;;
    esac
  done

  case "$url" in
    https://www.figma.com/*|https://figma.com/*|http://www.figma.com/*) ;;
    *) echo "isso não é um link do Figma: $url" >&2
       echo "peça ao usuário a URL do arquivo (figma.com/design/... ou figma.com/board/...)." >&2
       exit 1 ;;
  esac

  local file_key node_id
  file_key=$(printf '%s' "$url" | sed -nE 's#^https?://(www\.)?figma\.com/(file|design|board|proto|slides|deck)/([A-Za-z0-9_-]+).*#\3#p')
  node_id=$(printf '%s' "$url" | sed -nE 's/.*[?&]node-id=([^&]+).*/\1/p')

  if [ -z "$file_key" ]; then
    echo "não consegui extrair o file key de: $url" >&2
    echo "confirme com o usuário se o link é do arquivo, não de um comentário ou de uma busca." >&2
    exit 1
  fi

  # Nome do arquivo pela API REST — confirmação de que o link aponta para o que
  # o usuário acha que aponta. Falha aqui não impede o registro.
  local nome="" pasta="" token env_file="$RAIZ/.env"
  if [ -r "$env_file" ]; then
    token=$(sed -nE 's/^FIGMA_ACCESS_TOKEN=//p' "$env_file" | tr -d "\"'\r" | head -1)
    if [ -n "${token:-}" ]; then
      local meta
      meta=$(curl -s --max-time 15 -H "X-Figma-Token: $token" \
        "https://api.figma.com/v1/files/$file_key/meta" 2>/dev/null)
      nome=$(printf '%s' "$meta"  | sed -nE 's/.*"file":\{"name":"([^"]*)".*/\1/p')
      pasta=$(printf '%s' "$meta" | sed -nE 's/.*"folder_name":"([^"]*)".*/\1/p')
    fi
  fi

  mkdir -p "$(dirname "$ESTADO")"
  cat > "$ESTADO" <<FIM
{
  "url": "$(escapa "$url")",
  "fileKey": "$(escapa "$file_key")",
  "nodeId": "$(escapa "$node_id")",
  "nomeArquivo": "$(escapa "$nome")",
  "pasta": "$(escapa "$pasta")",
  "pagina": "$(escapa "$pagina")",
  "secao": "$(escapa "$secao")",
  "nota": "$(escapa "$nota")",
  "registradoEm": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
FIM

  echo "Destino registrado."
  echo "  arquivo : ${nome:-<nome não confirmado pela API>}${pasta:+  (pasta: $pasta)}"
  echo "  link    : $url"
  [ -n "$pagina" ] && echo "  página  : $pagina"
  [ -n "$secao" ]  && echo "  seção   : $secao"
  [ -n "$nota" ]   && echo "  nota    : $nota"
  [ -z "$nome" ] && echo "  aviso   : a API não confirmou o nome — cheque o token com /figma-status antes de construir."
  echo
  echo "Confirme que o Figma desktop está com ESTE arquivo aberto e em foco antes de use_figma/figma_execute."
  exit 0
}

# ---------------------------------------------------------------- show / clear

mostrar() {
  if [ -s "$ESTADO" ]; then cat "$ESTADO"; exit 0; fi
  echo "Nenhum destino registrado nesta sessão. Pergunte o link ao usuário." >&2
  exit 1
}

limpar() {
  # Compactação não é sessão nova — o destino confirmado continua valendo.
  if [ ! -t 0 ]; then
    case "$(cat)" in *'"source":"compact"'*|*'"source": "compact"'*) exit 0 ;; esac
  fi
  rm -f "$ESTADO"
  exit 0
}

# ---------------------------------------------------------------- despacho

case "${1:-}" in
  guard) guard ;;
  set)   shift; registrar "$@" ;;
  show)  mostrar ;;
  clear) limpar ;;
  *) echo "uso: figma-destino.sh {guard|set <link> [--pagina X] [--secao Y] [--nota Z]|show|clear}" >&2; exit 1 ;;
esac
