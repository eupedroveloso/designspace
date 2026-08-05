# Teste 2 — `/ref-ads-dna` no Nano Banana Pro — Seu Produto Pronto com IA

**Data:** 2026-08-03
**Objetivo:** repetir o teste do fluxo trocando o modelo de fechamento para **Nano Banana Pro**, que virou o default de criação por decisão do usuário.
**Escopo:** copy como contexto, imagem gerada. A copy não foi aplicada na peça.

## O que mudou em relação ao teste 1

- Modelo: `imagen-nano-banana-2` (Nano Banana Pro), geração direta, sem rascunho barato, porque a cena já estava decidida.
- Proporção: **4:5 nativo**, sem o desvio para 3:4 que o `seedream-5-pro` impõe.
- Resolução: `2k`.
- Categoria do DNA e tipo da Mandala trocados de propósito, para não repetir a peça anterior.

## Copy que originou a cena

**NA IMAGEM:** Enquanto você prepara, alguém publica.

**GANCHO:** Existe gente há dois anos organizando o lançamento que outra pessoa vai fazer neste fim de semana.

**DESENVOLVIMENTO:** A diferença aparece num ponto específico, o momento em que cada um decidiu que já dava para mostrar aquilo para alguém. Quem trava fica preso no loop de preparação: melhora o nome, refaz a capa, troca de plataforma, assiste mais uma aula sobre como estruturar módulos. Cada volta parece produtividade e nenhuma delas produz um produto que exista fora do computador.

O que quebra o loop é inverter a ordem da validação. Em vez de terminar o produto para depois anunciar, escreva o anúncio primeiro. O anúncio obriga a responder em três linhas para quem aquilo é, o que muda na vida da pessoa e quanto custa. Quando essas três linhas não fecham, o produto ainda não existe de verdade, e nenhuma aula gravada vai resolver isso. Quem escreve o anúncio na sexta descobre no sábado o que levaria dois meses para descobrir gravando módulo.

**CTA:** Dias 21 e 22 de agosto, das 10h às 18h, ao vivo. Lote 1 a R$ 97, com 7 dias para pedir reembolso. Garanta seu ingresso.

**HEADLINE (Meta Ads):** Enquanto você prepara, alguém publica.
**DESCRIÇÃO (Meta Ads):** Dois dias ao vivo para sair com produto, anúncio e página prontos.

## DNA visual aplicado

| Item do checklist | Decisão |
|---|---|
| Categoria | **D** — still de filme de ação hiper-realista, com metáfora física literal por baixo |
| Versão literal do conceito | A preparação vira uma parede física de papelada, e publicar vira atravessá-la |
| Luz | Contraluz duro estourando pelo buraco aberto, lado próximo do corpo em sombra com respingo ciano frio |
| Paleta | Carvão escuro e creme de papel, ciano como único acento; a camiseta petróleo amarra o invariante da marca |
| Formato | Vertical 4:5 nativo |
| Textura | Fibra de papel rasgado, papelão vincado, pele e suor no antebraço, trama da camiseta; fundo liso e desfocado |
| Contenção | Rosto sério, sem piscadela para o espectador, como manda a regra de humor por justaposição do board |

## Curadoria das três geradas

- **Vencedora, "atravessando a parede":** melhor ideia e melhor drama. O corpo em meio-passo entrega o verbo da headline, que é publicar.
- **Descartada, "soco na parede":** trouxe uma borda escura arredondada no enquadramento, tipo moldura de filme instantâneo. Defeito de render, não decisão de arte.
- **Alternativa guardada, "corredor de papelada":** composição mais limpa e simétrica, com respiro de sobra no topo, mas vira retrato em vez de ação. Guardada como opção para peça de tom mais sóbrio.

## Achados do teste

- **O Pro entrega 4:5 nativo.** O master saiu em 1856×2304 e precisou de um corte de 13 px na largura para virar 4:5 exato. Ficou muito melhor que o corte de 144 px que o `seedream-5-pro` exigiu no teste 1.
- **Salto real de qualidade fotográfica.** Luz, poeira suspensa, congelamento de movimento e microtextura de pele saíram em outro patamar. Justifica o Pro como default de fechamento.
- **A zona de respiro do DNA conflita com o sistema SPP.** O `ref-ads-dna` manda reservar espaço negativo no topo, e o `/anuncio-spp` ancora o bloco de texto em y≈652 com o CTA em y=956, ou seja, no terço inferior. Quando a peça for da SPP, o prompt deve pedir o respiro **embaixo**, não em cima. Vale registrar essa exceção na skill.
- Sem caractere legível e sem logo nas folhas, conferido em zoom a 100 %.

**Custo:** 225 créditos, três imagens em 2k.

## Entregáveis

- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-03-spp-parede-de-papelada-master-1856x2304.png`
- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-03-spp-parede-de-papelada-feed-1080x1350.jpg`
- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-03-spp-parede-de-papelada-alternativa-corredor.png`
