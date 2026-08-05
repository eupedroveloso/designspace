---
name: figma-status
description: Verifica a conexão com o Figma antes de qualquer trabalho no arquivo — conector MCP (OAuth), token REST e plugin Desktop Bridge. Use SEMPRE antes da primeira operação de Figma numa sessão, e sempre que uma chamada do Figma falhar, travar ou retornar erro de permissão/rate limit.
---

# Figma — check de status

Rode isto **antes da primeira operação de Figma em cada sessão**. Três camadas independentes; falham por motivos diferentes.

## 1. Conector MCP (OAuth)

```
mcp__claude_ai_Figma__whoami
```

Esperado: handle `Pedro Veloso`, email `pedrolucas@vtsd.com.br`, time **Ready To Go** (seat Full, tier pro).

Essa é a camada que as tools do MCP usam — `use_figma`, `get_design_context`, `create_new_file`, `upload_assets`. **Ela não usa o token do `.env`.** Se falhar, o problema é a autorização do conector: o usuário precisa reconectar em claude.ai → Settings → Connectors.

Também é o primeiro diagnóstico para rate limit.

## 2. Token REST

```bash
TOKEN=$(grep FIGMA_ACCESS_TOKEN "$CLAUDE_PROJECT_DIR/.env" | cut -d= -f2)
curl -s -w "\nHTTP %{http_code}\n" -H "X-Figma-Token: $TOKEN" https://api.figma.com/v1/me
```

Esperado: `HTTP 200` + o mesmo handle da camada 1.

- `403` — token inválido, expirado ou revogado. Peça um novo em Figma → Settings → Security → Personal access tokens.
- Handle diferente do MCP — as duas camadas estão em contas distintas. Pare e avise; escrever com uma conta e ler com a outra gera confusão silenciosa.

Serve para o que o MCP não cobre: listar projetos de um time, ler arquivo por ID, versões, comentários, webhooks.

**Nunca imprima o token.** Leia sempre do `.env`, jamais cole o valor em comando, log ou resposta.

## 3. Plugin Desktop Bridge

Não tem endpoint de ping — só se confirma tentando. Antes de `use_figma`, confirme com o usuário:

1. Figma **desktop** aberto (não o navegador)
2. O **arquivo alvo** aberto e em foco
3. O plugin **Desktop Bridge** rodando nesse arquivo

Sintoma típico: camadas 1 e 2 passam, `use_figma` trava ou dá timeout. Isso é bridge, não autenticação.

Após 2-3 falhas, **pare**. Reporte qual camada passou e qual falhou, e o que checar. Não repita a mesma chamada em loop.

## 4. Destino registrado

Conexão em pé não diz **onde** escrever. Antes de criar qualquer coisa:

```bash
.claude/hooks/figma-destino.sh show
```

Sem registro, um hook bloqueia toda tool de escrita — e o certo é justamente isso: pergunte o link ao usuário e registre com `/figma-destino`. Leitura não depende disso; as três camadas acima se checam sem destino nenhum.

## Saída

Uma linha por camada. Ex.:

```
MCP OAuth ✅ Pedro Veloso / Ready To Go (Full, pro)
REST      ✅ HTTP 200 — mesma conta
Bridge    ⚠️  não verificável — confirmar desktop + plugin antes de use_figma
Destino   ❌ não registrado — perguntar o link ao usuário (/figma-destino)
```
