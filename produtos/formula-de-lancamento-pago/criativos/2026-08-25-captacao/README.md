# 40 criativos de captação · Fórmula de Lançamento Pago

**Data:** 2026-08-25 · **Fase:** Captura · **Formato:** 1080×1080 (feed) · **Modelo:** GPT 2 (Magnific), o mais atual da família GPT
**Copy:** [copy-2026-08-25-captacao.md](copy-2026-08-25-captacao.md)

20 anúncios, cada um com um tipo diferente da Mandala de 18 Tipos, rodados em duas linhas visuais para teste A/B. Todo o texto foi renderizado pelo modelo de imagem, em português do Brasil.


## Onde cada coisa está

Estrutura padrão do projeto: conjunto, estilo, e dentro sempre `feed/` e `stories/`.

```
2026-08-25-captacao/
├── copy-2026-08-25-captacao.md    copy aprovada dos 20 anúncios
├── README.md                       este arquivo
├── linha-A-cartaz/
│   ├── feed/                       flp-01-A.png a flp-20-A.png
│   └── stories/                    ainda não produzido
├── linha-B-nativo/
│   ├── feed/                       flp-01-B.png a flp-20-B.png
│   └── stories/                    ainda não produzido
└── _contatos/                      folhas de contato, trabalho interno
```

A Linha B se chamava `linha-B-feed` e virou `linha-B-nativo` em 2026-08-26, porque `feed` agora é o nível de formato dentro de cada estilo. O conteúdo é o mesmo.

## As duas linhas

| | **Linha A — Cartaz** | **Linha B — Nativo** |
|---|---|---|
| Direção de arte | publicidade impressa autoral | conteúdo nativo, baixa produção |
| Paleta | creme `#EEEBE6` · espresso `#2C140D` · tijolo `#E0341F` | cor de ambiente real, sem grading |
| Chave de luz | gráfica, dura, direcional de cartaz | janela, lâmpada de casa, tela de laptop |
| Ângulo | composição frontal desenhada | celular na mão, selfie, top-down |
| Tipografia | grotesca black, caixa alta, tracking negativo | sans simples, caixa baixa, tipo story |
| Tratamento do texto | integrado ao design impresso, faixa de serviço na base | caixa branca ou preta sobreposta |

As seis alavancas de distinção do `CLAUDE.md` mudam entre A e B. É isso que atende a exigência de variedade visual do Andromeda no Meta Ads.

## Mapa de execução

| # | Tipo da Mandala | Headline na imagem | Formato — Linha A | Formato — Linha B |
|---|---|---|---|---|
| 01 | Revelação | O produto que vende é o que existe | HQ / quadrinho | selfie UGC na cozinha |
| 02 | Comparação | Seis meses estudando. Três dias publicando. | flyer rasgado em duas metades | mesa dividida, top-down |
| 03 | Problema/Solução | Chega sem produto. Sai com um. | render 3D tipo brinquedo | selfie no sofá |
| 04 | Certo/Errado | Primeiro a oferta. Depois a plateia. | cartaz de cinema, palco | quarto virado estúdio |
| 05 | Explicação | Por que dá pra vender sem lista | still-life conceitual, fichário × celular | celular na mão, gerenciador |
| 06 | Curiosidade | R$ 97 e a conta que ninguém faz | tipografia protagonista, calculadora | guardanapo com a conta |
| 07 | Reflexão | Nunca foi tão barato montar um negócio | gravura de jornal antigo | rua, loja fechada |
| 08 | Demonstração | A conta que diz se vale anunciar | balança conceitual | planilha no laptop |
| 09 | Procedimento | Três dias. Três entregas. Um negócio. | HQ de três painéis | post-its na geladeira |
| 10 | Impacto Visual | 212 prints salvos. Zero link no ar. | caricatura, avalanche de prints | galeria do celular |
| 11 | Oportunidade | Você já tem o conteúdo. Falta empacotar. | render 3D tipo brinquedo | áudio de WhatsApp no carro |
| 12 | História | Ele montou o produto em dois dias | key art de drama | madrugada no laptop |
| 13 | Prova Social | A primeira venda caiu durante o evento | escala impossível, notificação gigante | notificação na mão |
| 14 | Clickbait | Comprei 14 cursos de IA. Faturei zero. | caricatura, pilha de caixas | deadpan na frente da tela |
| 15 | Sensação | O barulhinho da primeira venda | still gráfico, ondas de som | cozinha escura, 22h47 |
| 16 | Contraste | Duas segundas-feiras bem diferentes | HQ de dois painéis | duas fotos empilhadas |
| 17 | Ensino | Como saber se o anúncio se paga | diagrama desenhado à mão | caderno com a conta |
| 18 | Dilema | Três dias travados ou mais seis meses | cartaz, bifurcação de portas | calendário de parede |
| 19 | Certo/Errado | IA pra postar ou pra montar negócio | render 3D, linha de montagem | abas de IA abertas |
| 20 | Revelação | Não fica gravado. E esse é o ponto. | still gráfico, VHS monumental | grade de chamada ao vivo |

## Auditoria de distinção visual, medida

Matiz média e luminância média comparadas peça a peça, com o limiar do `CLAUDE.md` (matiz a menos de 20° somada a luminância a menos de 0,05 significa que as duas pareceriam irmãs no feed).

**18 dos 20 pares A × B passam com folga.** Dois pares ficam dentro do limiar numérico:

- **09** (dmatiz 5,4 · dlum 0,012)
- **15** (dmatiz 16,7 · dlum 0,029)

Nos dois casos a direção de arte separa as peças de forma que a métrica de cor não enxerga: 09-A é uma tira de quadrinhos em três painéis contra uma foto de geladeira com post-its; 15-A é um still gráfico de ondas de som contra uma foto noturna de cozinha. Ficam no ar. Se aparecerem lado a lado no mesmo conjunto e incomodarem, o ajuste é trocar o acento da versão A para o amarelo `#F2C744`.

**Dentro da Linha A**, 39 pares ficam abaixo do limiar, e isso é esperado: a linha tem paleta travada em três cores, é o que a torna uma linha. A variedade dentro dela vem do formato, não da cor. Se o conjunto pedir mais espalhamento cromático interno, dá pra girar o acento por peça entre tijolo, laranja `#F2803C` e amarelo `#F2C744` sem perder a assinatura.

## Uma peça foi refeita

A **16-B** saiu na primeira rodada como uma foto única, perdendo a comparação que a copy exige. Foi regerada como duas fotos empilhadas e substituída.
