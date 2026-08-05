---
name: brand-kit
description: Consolida a identidade de um cliente/projeto em brand/<cliente>.md e monta a página de guidelines no Figma. Use ao começar com um cliente novo, ao formalizar uma identidade que existe só na cabeça de alguém, ou quando brand-guardian avisar que não há kit para auditar.
---

# Brand kit

Objetivo: um arquivo que todo agente lê para não precisar perguntar de novo — e uma página no Figma que o cliente reconhece como o manual.

## Passos

### 0. Pergunte onde as guidelines nascem
Link do arquivo Figma, pelo usuário, nesta sessão. Rode `/figma-destino` e registre. Arquivo de referência que você leu para extrair paleta não vira arquivo de destino por tabela.

### 1. Reúna o que já existe
Varra `assets/` (logos, artes antigas), peças anteriores em `outputs/`, e o que o usuário fornecer. Se houver arquivo Figma de referência, extraia com `get_variable_defs` e `get_design_context` — cores e tipografia reais valem mais que descrição de memória.

### 2. Preencha as lacunas
Só o que faltar. Para exploração de direção estética, use `/moodboard` — não invente paleta sozinho.

Extraia cor de logo/arte existente em vez de estimar a olho. Se precisar vetorizar um logo raster, `images_to_svg`.

### 3. Escreva `brand/<cliente>.md`

```markdown
# Brand kit — <Cliente>

**Atualizado:** YYYY-MM-DD

## Essência
O que a marca é, em duas frases. O que ela não é, em uma.

## Paleta
| Papel | Nome | Hex | Uso |
|---|---|---|---|
| Primária | | #______ | |
| Secundária | | #______ | |
| Acento | | #______ | |
| Neutros | | #______ | |
| Semânticas | sucesso / alerta / erro | #______ | |

Pares de contraste aprovados (AA): texto #___ sobre #___ = __:1

## Tipografia
| Papel | Família | Pesos | Escala |
|---|---|---|---|
| Display | | | |
| Corpo | | | |
| Mono | | | |

## Logo
Versões disponíveis, fundo permitido para cada, área de respiro (em múltiplos de X), tamanho mínimo.

## Tom visual
Fotografia: estilo, luz, enquadramento, tratamento de pele/cor.
Ilustração: estilo, traço, uso de cor.
Mood em 5 palavras.

## Prompt base (Magnific)
Trecho reutilizável que ancora qualquer geração nessa identidade — paleta, luz, estilo, mood.

## Do / Don't
- ✅ …
- ❌ …
```

A seção **Prompt base** é o que faz o kit trabalhar: `visual-generator` cola ela em toda geração e a marca sai consistente sem ninguém lembrar.

### 4. Monte a página no Figma
Delegue ao `figma-builder` (`/figma-use` + `/figma-generate-library`). Além da página visual de guidelines, crie as **variáveis** — cor, tipografia, spacing. Guideline que não vira token não é usado.

### 5. Registre
Aponte o brand kit no `CLAUDE.md` do projeto se ele for o cliente principal.

## Regra

Kit é documento vivo. Quando uma peça aprovada contrariar o kit, atualize o kit ou corrija a peça — nunca deixe os dois divergirem em silêncio.
