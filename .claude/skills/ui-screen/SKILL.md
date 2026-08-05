---
name: ui-screen
description: Monta uma tela de produto no Figma a partir de descrição, fluxo ou referência — usando componentes e tokens do design system existente. Use para "cria a tela de checkout", "monta o dashboard no Figma", "desenha esse fluxo", telas de app/web, modais, painéis.
---

# UI screen

Objetivo: tela que o time consegue editar e evoluir — componentes do DS, tokens amarrados, auto-layout. Não um desenho bonito e morto.

## Passos

### 0. Pergunte onde a tela nasce
Link do arquivo Figma, página e seção — pelo usuário, nesta sessão. Rode `/figma-destino` e registre antes de qualquer coisa. Um hook bloqueia a escrita enquanto não houver destino.

### 1. Carregue as skills do Figma
`/figma-use` **sempre**, junto com `/figma-generate-design` (tela composta) ou `/figma-generate-library` (se precisar criar componentes que ainda não existem). Sem isso, `use_figma` falha de forma difícil de debugar.

### 2. Levante o design system antes de desenhar
- `get_libraries` — bibliotecas disponíveis
- `search_design_system` — busque cada componente que a tela pede (botão, input, card, nav, tabela…)
- `get_variable_defs` — cores, espaçamento, tipografia, raio

**Reusar ganha de criar.** Só construa componente novo quando a busca não achou nada equivalente — e nesse caso construa direito: variantes, propriedades, variáveis amarradas.

Se não existe design system, pare e proponha `/brand-kit` + fundação de tokens primeiro. Tela montada sobre valores hardcoded é dívida imediata.

### 3. Estruture antes de preencher
Defina hierarquia: layout base → seções → componentes → conteúdo. Grid e breakpoint definidos antes do primeiro nó.

### 4. Monte seção por seção
Uma seção por vez, `get_screenshot` entre etapas para conferir. Não tente a tela inteira numa chamada.

Inegociáveis:
- **Auto-layout em tudo.** Posicionamento absoluto quebra na primeira edição.
- **Token, nunca hex solto.** Cor, spacing, tipografia e raio vêm de variável.
- **Nomes reais nos layers.** `Header / Nav / Actions`, não `Frame 47`.
- **Conteúdo plausível.** Nomes, valores e datas realistas — lorem ipsum esconde problema de layout.

### 5. Cubra os estados
Tela só com o estado feliz não serve para desenvolvimento. Inclua o que a tela realmente tem: vazio, carregando, erro, e os estados dos componentes interativos (hover, focus, disabled, selecionado).

### 6. Feche
Rode `brand-guardian` se a tela vai para cliente. Cheque contraste dos textos.

## Saída

Link do arquivo/frame + componentes do DS reusados + componentes novos criados + estados cobertos + o que ficou pendente. Registre em `outputs/`.
