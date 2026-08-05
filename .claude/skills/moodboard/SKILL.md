---
name: moodboard
description: Constrói um moodboard de direção visual — gera ou coleta referências e monta em grid organizado no Figma/FigJam. Use quando o projeto precisa alinhar direção estética antes de produzir a peça final, ou quando o usuário pede "referências", "moodboard", "direção visual", "estudo de estilo".
---

# Moodboard

Objetivo: alinhar estética **antes** de gastar em produção final. Um moodboard bom mata discussão; um moodboard genérico só adia.

## Passos

### 0. Pergunte onde o moodboard nasce
Link do arquivo Figma ou FigJam, pelo usuário, nesta sessão. Rode `/figma-destino` e registre antes de gerar a primeira referência — não depois, quando já queimou crédito.

### 1. Defina os eixos
Leia o brief. Escolha **2-3 direções distintas e nomeadas** — não 12 imagens aleatórias. Ex.: "Editorial sóbrio", "Pop saturado", "Orgânico artesanal". Direções que se parecem não são direções.

### 2. Reúna as referências
Duas fontes, combine livremente:

- **Stock** — `stock_search` para fotografia real existente. Barato e rápido.
- **Geração** — lance `visual-generator` em paralelo, **um agente por direção**, 3-4 imagens cada, em modelo rápido (`recraft-v4-1` ou `imagen-nano-banana-2-lite`). Moodboard é exploração; não use modelo caro.

Inclua também paleta e amostra tipográfica de cada direção — moodboard só com foto não decide nada.

### 3. Monte no Figma
Carregue `/figma-use` (e `/figma-use-figjam` se for FigJam) antes de escrever. Delegue ao `figma-builder`.

Layout por direção, em coluna ou seção:
- Título da direção + uma frase do que ela comunica
- Grid 3-4 de imagens (auto-layout, gap consistente)
- Faixa de paleta com os hex visíveis
- Amostra tipográfica: display + corpo
- Linha "funciona para / não funciona para"

FigJam serve bem quando o cliente vai comentar e votar. Arquivo de Design serve quando vira base da produção.

### 4. Feche com recomendação
Não entregue as direções em pé de igualdade. Diga qual você recomenda e por quê, ancorado no objetivo do brief.

## Saída

Link do arquivo + as direções nomeadas + sua recomendação. Registre em `outputs/`.
