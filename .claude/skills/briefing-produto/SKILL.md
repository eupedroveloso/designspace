---
name: briefing-produto
description: Cria ou atualiza o briefing completo de um produto extraindo tudo de uma landing page (URL) ou de um arquivo Figma — nome, promessa, datas, preço, como funciona, bônus, garantia, público, nicho, paleta de cores, família tipográfica e logo em SVG. Use antes de qualquer criação de copy ou criativo, e sempre que o usuário mencionar um produto novo.
---

# Briefing de produto

Primeira etapa de tudo. **Nenhuma copy e nenhum criativo começa sem o briefing do produto na mão.**

Saída: `produtos/<slug-do-produto>/briefing.md`, mais os assets de identidade extraídos.

---

## Passo 1 — Qual produto

**Sempre pergunte antes de começar:**

```
Para qual produto é essa criação?

<lista os produtos já existentes em produtos/>

Ou digite o nome de um produto novo.
```

- **Produto existe** → carregue `produtos/<slug>/briefing.md` e confirme em uma linha o que vai usar. Pergunte se algo mudou (data, preço, oferta) antes de seguir.
- **Produto não existe** → siga para o Passo 2 e crie a pasta.

Slug: minúsculas, sem acento, hífen no lugar de espaço. `Seu Produto Pronto com IA` → `seu-produto-pronto-com-ia`.

---

## Passo 2 — Fonte da extração

```
De onde eu extraio as informações?

1. Link da landing page
2. Link do Figma (arquivo ou node da página)
3. Os dois
4. Não tenho link, vou passar as informações
```

Peça o link. Com os dois, a LP manda no conteúdo e o Figma manda na identidade visual.

---

## Passo 3 — Extração da landing page

Use `WebFetch` na URL. Se a página for pesada ou dividida em seções, busque também as âncoras (`/#oferta`, `/#faq`).

Extraia, e marque como `não encontrado` o que não achar — **nunca invente**:

| Campo | O que procurar |
|---|---|
| Nome do produto | título, logo, `<title>`, headline principal |
| Promessa | headline e subheadline do topo |
| Formato | imersão, curso, mentoria, evento, workshop; ao vivo ou gravado |
| Datas e horário | seção de agenda, contagem regressiva, "dias 21 e 22" |
| Canal | Zoom, YouTube, presencial, área de membros |
| Preço | valor cheio, valor promocional, parcelamento, lote |
| Como funciona | seção de método, etapas, cronograma, o que acontece em cada dia |
| O que a pessoa leva | entregáveis, bônus com ancoragem de preço |
| Garantia | prazo e condição |
| Público | "para quem é" / "para quem não é" |
| Autoridade | quem ensina, números e conquistas concretas |
| Prova | depoimentos com resultado, números de alunos |
| CTA | texto do botão e destino |
| FAQ | objeções que a página já responde |

**Identidade visual pela LP:**
- **Paleta** — busque as CSS custom properties (`--color`, `--primary`) no HTML. Se não houver, baixe o screenshot e amostre as cores dominantes por frequência.
- **Tipografia** — procure `font-family` no CSS e os `<link>` do Google Fonts.
- **Logo** — ache o `<img>` ou `<svg>` do cabeçalho. Se for SVG, baixe o arquivo. Se for PNG/JPG, baixe e vetorize com `images_to_svg` do Magnific.

---

## Passo 4 — Extração do Figma

Carregue `/figma-status` antes. Depois:

- `get_variable_defs` — cores, tipografia, espaçamento como variáveis. É a fonte mais confiável de paleta.
- `get_design_context` no node da página — estrutura, textos, estilos aplicados.
- `get_screenshot` — leitura visual e amostragem de cor quando não houver variáveis.
- `get_metadata` — encontrar o node do logo pelo nome.
- **Logo em SVG:** localize o node do logo e exporte com `download_assets` em formato SVG.

Se a paleta vier de variáveis, registre o nome da variável junto do hex — isso permite reusar o token depois.

---

## Passo 5 — Nicho

Deduza o nicho do conteúdo extraído: mercado, público, vocabulário, tipo de dor. Registre também os **sub-nichos** que a campanha pode segmentar (ex.: infoproduto → dentista, nutricionista, advogado).

O nicho define a pesquisa de referências visuais na etapa seguinte, então seja específico. "Saúde" não serve; "odontologia, dentista dono de consultório" serve.

---

## Passo 6 — Escrever o briefing

Crie a estrutura:

```
produtos/<slug>/
├── briefing.md
├── identidade/
│   ├── logo.svg
│   ├── paleta.md
│   └── tipografia.md
└── criativos/
```

`briefing.md` no formato:

```markdown
# <Nome do produto>

**Atualizado:** AAAA-MM-DD
**Fontes:** <URL da LP> · <link do Figma>
**Nicho:** <nicho principal> · sub-nichos: <lista>

## Promessa
<uma frase, do jeito que a página promete>

## Formato
<imersão / curso / evento> · <ao vivo / gravado> · <duração> · <canal>

## Datas
<datas e horários, ou "não encontrado">

## Preço
| Item | Valor |
|---|---|
| Cheio | |
| Promocional | |
| Parcelamento | |
| Lote atual | |

## Como funciona
<etapas, cronograma, o que acontece em cada dia>

## O que a pessoa leva
- <entregável> — <ancoragem de preço, se houver>

## Garantia
## Público
**Para quem é:** · **Para quem não é:**

## Autoridade
<quem ensina, números concretos>

## Prova
<depoimentos com resultado, números>

## CTA
<texto do botão> → <destino>

## Objeções que a página responde
## Quadro e Decorado
**Quadro:** <transformação técnica>
**Decorado:** <consequência na vida>

## Lacunas
<o que não foi encontrado e precisa ser confirmado com o usuário>
```

`identidade/paleta.md`: tabela com papel, hex, nome da variável e onde é usada. `identidade/tipografia.md`: famílias, pesos, escala e papel de cada uma.

---

## Passo 7 — Fechar

Mostre ao usuário um resumo curto: nome, promessa, formato, datas, preço, nicho, e **a lista de lacunas**. Peça confirmação das lacunas antes de seguir para a copy.

Só depois disso o fluxo segue: `/copy-anuncio` → pesquisa de referências do nicho → design.
