# SPP com IA — dois anúncios teste com o rosto do Leandro Ladeira

**Data:** 2026-08-05
**Produto:** seu-produto-pronto-com-ia
**Arquivo:** `Seu-Produto-Pronto` · página **`+++TESTE IA +++`** (`2518:147`)
**Frames:** `AD-LADEIRA-A-TOPO-1080x1350` (`2830:30`) · `AD-LADEIRA-B-FUNDO-1080x1350` (`2830:31`)
**Formato:** 1080×1350, uma peça cada, `imagen-nano-banana-2`, referências de rosto de `assets/leandro-ladeira/`

---

## Copy

**A — Topo · tipo Revelação**

| | |
|---|---|
| Head | Produzir ficou rápido. / Decidir trava. |
| Subhead | Aula, anúncio e página saem em minutos. |
| CTA | Clique em "Saiba mais" e veja o que muda |

**B — Fundo · tipo Demonstração**

| | |
|---|---|
| Head | No segundo dia, / o anúncio já roda. |
| Subhead | 21 e 22 de agosto, ao vivo. Você chega sem nada e sai vendendo. |
| CTA | Clique em "Saiba mais" e garanta sua vaga |

Sem a porcentagem de ingressos vendidos, conforme a restrição do briefing. Duração sempre em 2 dias.

---

## Registro de distinção visual

As seis alavancas, para a próxima peça da campanha não repetir:

| Alavanca | A — Topo | B — Fundo |
|---|---|---|
| Paleta e temperatura | frio azul-acinzentado | quente âmbar |
| Chave de luz | low-key, monitor lateral duro, queda para a base | high-key, sol duro de manhã pela direita |
| Ângulo de câmera | altura dos olhos, 50 mm | levemente de cima, 28 mm |
| Tipografia | Albert Sans ExtraBold 72 / Regular 38 | Albert Sans ExtraBold 60 / Regular 38 |
| Tratamento do texto | branco sobre base quase preta, acento `#46ABEC` | tinta `#100A0D` sobre parede clara, sem acento |
| Direção de arte | retrato conceitual, parede de opções | cena doméstica flagrada |

Seis de seis trocadas. Figurino: camiseta grafite (A) e camisa de linho areia (B).

---

## Auditoria de contraste, pior caso medido

| Peça | Faixa | Razão | Desvio do fundo | Piso aplicável | Veredito |
|---|---|---|---|---|---|
| A | Head linha 1 (branco) | 14,62:1 | 0,073 | 4,5:1 | ok |
| A | Head linha 2 (acento azul) | 7,39:1 | 0,034 | 3:1 | ok |
| A | Subhead | 14,31:1 | 0,067 | 4,5:1 | ok |
| A | CTA | 18,04:1 | 0,081 | 7:1 | ok |
| B | Head | 8,44:1 | 0,101 | 7:1 | ok |
| B | Subhead | 9,19:1 | 0,181 | 7:1 | ok |
| B | CTA | 9,49:1 | 0,213 | 7:1 | ok |

**Observação que fica em aberto na B:** o desvio do fundo nas três faixas está entre 0,10 e 0,21, bem acima do limite de 0,05 que o `revisor-final` pede para fundo homogêneo. A razão de contraste passa com folga, mas as diagonais de sol na parede tornam o fundo movimentado. Vale como AJUSTAR, não como bloqueio.

---

## Decisões tomadas no caminho

- **A foto se ajustou ao texto, não o contrário.** A primeira versão da A tinha só 340 px de faixa livre, o que jogaria a headline para 66 px. A cena foi expandida para 9:16 no Magnific, recortada mais abaixo e a headline voltou para 72 px.
- **O acento quente da B foi removido por medição.** `#8A2A08` sobre a parede dava 3,74:1 contra os 7:1 exigidos pelo desvio. Um laranja escuro o bastante para passar seria indistinguível de preto, então a hierarquia da headline ficou por peso.
- **A B foi regerada uma vez.** A primeira composição punha o assunto no centro e deixava só 540×337 px de zona calma. O reenquadramento pediu o assunto no terço direito e a metade esquerda vazia.
- **Nenhum escurecimento global, nenhum halo, nenhuma sombra de texto.** As duas passam sem auxílio de contraste.

## Pendências

- **Story 9:16** ainda não derivado. Sai por `/ad-set` assim que o feed for aprovado.
- **`.env` não existe no projeto**, então a camada REST do Figma está fora e a auditoria usou o screenshot do nó em vez do PNG exportado pela API.
