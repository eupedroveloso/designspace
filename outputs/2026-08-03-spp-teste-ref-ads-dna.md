# Teste do fluxo com `/ref-ads-dna` — Seu Produto Pronto com IA

**Data:** 2026-08-03
**Objetivo:** validar a skill `ref-ads-dna` recém-instalada dentro do fluxo obrigatório de criação de anúncio.
**Escopo:** copy como contexto, imagem gerada. A copy não foi aplicada na peça.

## Decisões assumidas (sem confirmação do usuário, por ser teste)

- Produto: `seu-produto-pronto-com-ia` (único cadastrado em `produtos/`)
- Campanha: pico de vendas, fase **Venda** (evento em 21 e 22/08, lote 1 a R$ 97, LP manda direto pro checkout)
- Formato: imagem estática, feed
- Tipo da Mandala escolhido para a peça: **Revelação**

## Copy que originou a cena

**NA IMAGEM:** Sua ideia não morreu. Ela travou.

**GANCHO:** A maior parte dos produtos digitais que nunca foram vendidos já estava pronta na cabeça do dono.

**DESENVOLVIMENTO:** O que separa a ideia do arquivo é uma fila de decisões pequenas que ninguém ensina a tomar. Qual formato, qual preço, quantos módulos, o que entra na primeira aula, o que vira bônus. Cada uma dessas trava a pessoa por uma semana, e quando a semana passa a ideia já esfriou e a próxima já chegou. É assim que se forma o produto de gaveta, aquele que existe inteiro na cabeça e em lugar nenhum além dela.

A ordem que destrava é o contrário da que a maioria segue. Primeiro se define para quem, depois a promessa, depois o preço, e só então o conteúdo. Quem começa pelo conteúdo escreve quarenta slides para descobrir no fim que o produto cabe em R$ 47 e não paga o esforço. Quem começa pela promessa escreve só o que a promessa exige, e termina.

**CTA:** Dias 21 e 22 de agosto, das 10h às 18h, ao vivo. Lote 1 a R$ 97, com 7 dias para pedir reembolso. Garanta seu ingresso.

**HEADLINE (Meta Ads):** Sua ideia não morreu. Ela travou.
**DESCRIÇÃO (Meta Ads):** Dois dias ao vivo para sair com produto, anúncio e página prontos.

## DNA visual aplicado

| Item do checklist | Decisão |
|---|---|
| Categoria | **E + B** — escala impossível resolvendo metáfora física literal |
| Versão literal do conceito | A gaveta onde a ideia morre vira a fábrica que entrega o produto |
| Luz | Lateral dura vinda da esquerda alta, mais o brilho ciano da própria linha de montagem como segunda fonte |
| Paleta | Carvão escuro + madeira quente, ciano como único acento (ancorado no `#46ABEC` da marca) |
| Zona de respiro | Terço superior escuro e vazio, reservado para o headline |
| Formato | Vertical |
| Textura | Veio e riscos da madeira, metal escovado das máquinas, fibra do papel amassado; fundo liso e desfocado |

## Produção

1. Exploração em `imagen-nano-banana-2-lite`, três cenas concorrentes, duas imagens cada (180 créditos): fábrica na gaveta, ampulheta despejando caixas prontas, rascunho amassado ao lado da caixa lacrada.
2. Vencedora: **fábrica na gaveta**. A ampulheta perdia a leitura das caixas e a dupla rascunho/caixa ficava com densidade baixa demais para feed.
3. Refino em `seedream-5-pro` usando o draft vencedor como referência de imagem, duas variações (200 créditos).

**Custo total:** 380 créditos.

## Entregáveis

- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-03-spp-fabrica-na-gaveta-master-1728x2304.jpg`
- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-03-spp-fabrica-na-gaveta-feed-1080x1350.jpg`

## Achados do teste

- **`seedream-5-pro` não aceita 4:5.** A chamada foi ajustada sozinha para 3:4. O master saiu em 3:4 e o corte para 1080×1350 foi feito depois, cortando pela base para preservar a zona de respiro do topo. Vale considerar registrar isso na tabela de modelos do `CLAUDE.md`.
- O preview do Magnific volta quadrado mesmo quando o render respeita a proporção pedida. Conferir sempre o arquivo final, não a miniatura.
- A regra de "nenhum texto legível" passou: os papéis da gaveta têm rabisco de escrita e um esboço, sem caractere legível nem logo.
