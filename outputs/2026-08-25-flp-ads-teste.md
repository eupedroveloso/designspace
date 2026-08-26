# Fórmula de Lançamento Pago · Lote de teste (v4)

**Data:** 2026-08-25
**Produto:** `produtos/formula-de-lancamento-pago/`
**Copy:** `produtos/formula-de-lancamento-pago/copy/anuncios-meta-estatico-captura-flp.md`
**Fase:** pico de vendas · Captura · topo de funil
**Público:** iniciante total no digital, que ainda não sabe que o lançamento pago existe

---

## Estado

| Peça | Estilo | Feed 1080×1350 | Story 1080×1920 |
|---|---|---|---|
| **AD 01** | Cartoon / HQ, Erico e Ladeira ilustrados | entregue | **bloqueado** |
| **AD 02** | UGC real, pessoa comum | entregue | **bloqueado** |

Os stories dependem do preenchimento generativo do Magnific (`images_expand`). O endpoint respondeu uma única vez no começo da sessão e passou a devolver erro de conexão em todas as tentativas seguintes, ao longo de cerca de 40 minutos. O resto da API do Magnific segue funcionando normalmente, então é falha específica dessa rota.

**Alternativas testadas e descartadas:**
- `design_auto_resize` para 9:16 — duplicou a pill de data, estourou o texto para fora da margem direita, perdeu o contorno da pill e devolveu 768×1376.
- Montagem local esticando o feed — foi exatamente o que o usuário reprovou.

## Ajustes aplicados na v4

7. **Mockup real no lugar do placeholder.** A tela do notebook do AD 02 deixou de mostrar barras cinzas e passa a exibir uma página de vendas resolvida do produto **dela**: capa laranja com a foto da própria mulher segurando uma marmita, headline "MARMITAS DA SEMANA", três miniaturas de pratos e botão verde "QUERO O MEU". Regra nova em `CLAUDE.md`, seção "Produto digital na cena é mockup de verdade".

## Ajustes aplicados na v3

5. **Mancha da subhead na largura da head.** Razão medida: **0,94** no AD 01 e **0,99** no AD 02, contra 0,80 e 0,82 da rodada anterior. O piso da regra é 0,90. O que resolveu foi descrever a coluna de texto como um retângulo invisível e exigir que toda linha corra até quase encostar na borda direita dele, em vez de pedir "não quebre linha cedo".
6. **Cena do UGC amarrada à copy.** A peça mostra o notebook virado para a câmera com a página de vendas publicada na tela, e o caderno de rascunho manuscrito de lado na mesa. Lê o "chega sem produto e sai com o lançamento no ar" sem depender do texto. A tela usa blocos e barras de placeholder, sem palavra legível, conforme a regra de ouro 5.1.

## Ajustes aplicados na v2

1. **Copy reescrita com foco na oportunidade.** AD 01 explica a mecânica do lançamento pago (o público vem do tráfego, não da audiência acumulada). AD 02 ancora o preço contra o retorno e enquadra como evento de implementação.
2. **Repertório absorvido dos ads anteriores da conta:** pill de data com contorno coral e tipografia monospace, moldura verbal de "evento de implementação", linha que inclui quem já está e quem ainda não entrou no digital, e o CTA no padrão da casa.
3. **CTA escrito, sem botão.** `Clique em Saiba mais e garanta seu ingresso`, em coral, sem caixa nem retângulo atrás.
4. **Cartoon sem borda.** Arte sangra até as quatro extremidades.

## Margens medidas

| Peça | Esquerda | Direita | Topo | Base |
|---|---|---|---|---|
| AD 01 feed | 142 px | 159 px | — | 97 px |
| AD 02 feed | 115 px | 401 px | 93 px | — |

Como foram obtidas, já que o modelo não obedece pedido de margem em prosa:
- **AD 01:** faixa preta chapada alongada em 100 px por baixo (invisível, é preto liso) e laterais espelhadas em 91 px. O campo coral de quadrinho espelha de forma plausível, sem emenda perceptível.
- **AD 02:** 60 px removidos da base (mesa vazia) e a faixa de 80 px de parede lisa na aresta esquerda esticada para 134 px, o que empurra o bloco de texto para dentro. Parede desfocada não denuncia esticamento.

## Distinção visual

| | AD 01 HQ | AD 02 UGC |
|---|---|---|
| Paleta | coral saturado sobre preto | neutro claro, branco quente e cinza |
| Chave de luz | luz dura de quadrinho | luz de janela difusa, high key |
| Ângulo | contra-plongée | altura dos olhos, selfie |
| Tipografia | display pesado, caixa alta | sans limpa, caixa mista |
| Alinhamento | texto à esquerda, embaixo | texto à direita, em cima |
| Direção de arte | ilustração HQ | fotografia crua |

Seis de seis alavancas trocadas.

## Conformidade

Nenhuma peça usa promessa de ganho. As expressões de faturamento presentes nos ads anteriores da conta ("maior faturamento da sua vida") ficaram de fora do criativo de topo de funil, porque afirmação de renda nessa categoria costuma ser reprovada pelo Meta. Reservadas para remarketing com o aviso legal visível.

## Fila

- **Stories** dos dois, assim que o `images_expand` voltar.
- **3D / caricatura** e **flyer publicitário**, os outros dois estilos marcados.

Regra fixa em `identidade/uso-dos-mentores.md`: quando a peça usa o rosto de um dos dois, os dois aparecem juntos. Não vale em UGC.
