---
name: brief
description: Transforma um pedido solto de design em um brief estruturado salvo em briefs/. Use no início de qualquer tarefa que vá gerar imagem ou montar arquivo no Figma, quando o pedido chegou vago ("faz um banner pro lançamento"). Evita queimar crédito gerando a coisa errada.
---

# Brief

Objetivo: sair de "faz um banner" para um documento que qualquer agente consegue executar sem adivinhar.

## Passos

1. **Leia o contexto existente** — `brand/` (kits disponíveis), `briefs/` (tarefas parecidas já feitas), `assets/` (o que o usuário já forneceu).

2. **Preencha o que der sozinho.** Se o cliente tem brand kit, paleta/tipografia/tom já estão resolvidos — não pergunte de novo.

3. **Pergunte só o que muda a execução.** No máximo 3-4 perguntas, via `AskUserQuestion`. Candidatas boas: objetivo da peça, público, canal/formato, prazo, o que não pode aparecer. Candidatas ruins: qualquer coisa que você consegue inferir ou decidir com bom senso.

4. **Escreva o brief** em `briefs/YYYY-MM-DD-cliente-tarefa.md`:

```markdown
# <Tarefa> — <Cliente>

**Data:** YYYY-MM-DD
**Tipo:** UI/Produto | Marketing | Branding
**Brand kit:** brand/<arquivo>.md  (ou: nenhum — criar antes)

## Objetivo
O que essa peça precisa fazer acontecer. Uma frase.

## Público
Quem vê e em que estado mental.

## Entregáveis
- Formato / dimensão / canal, um por linha

## Direção visual
Mood, referências, paleta, tipografia. Ancorado no brand kit.

## Restrições
Prazo, o que não pode aparecer, exigências legais, limites técnicos.

## Suposições
O que eu decidi sem confirmar. O usuário corrige aqui se eu errei.

## Pipeline
Ex.: /copy-card (fase: Meio, 3 variações) → visual-generator (background, recraft-v4-1)
     → figma-builder (montagem + variações) → brand-guardian (auditoria)
```

Se a peça tem texto, `/copy-card` vem **antes** do visual: a Head define o enquadramento da imagem. Registre a fase do funil no brief — é o dado que mais muda a execução.

5. **Confirme em uma linha** e siga direto para a execução — não espere aprovação formal a menos que as suposições sejam pesadas.

## Regra

Brief que não cabe em uma tela é brief que ninguém lê. Corte tudo que não muda uma decisão de execução.
