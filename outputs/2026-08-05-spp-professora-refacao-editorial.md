# SPP · Professores — refação das 3 peças pelo método de design editorial

**Data:** 2026-08-05
**Produto:** Seu Produto Pronto com IA · evento 21 e 22 de agosto
**Motivo:** o usuário reprovou as três peças. Primeiro teste do método novo (`references/design-editorial.md` + `scripts/analise-composicao.py`).
**Nós:** `2662:1093` A-VERDE · `2662:1058` B-MESA (era B-FLATLAY) · `2662:1059` C-MONO

---

## O que estava errado, medido

| Peça | Queixa do usuário | Número que confirmou |
|---|---|---|
| C-MONO | "texto no topo, imagem à direita — devia ser texto à esquerda" | zona livre de **360 × 708 px** com energia 0,001 desperdiçada; centro de massa em x 74 % |
| B-FLATLAY | "o contraste ficou muito ruim" | chapéu laranja a **1,43:1** no pior caso; **nenhuma** faixa da foto alcançava o piso de 7:1 (melhor: 5,09:1) |
| A-VERDE | "enquadrou mal, ela quase embaixo do texto" | texto na faixa de desvio **0,20**, a mais movimentada da peça, com os 270 px mais calmos vazios no topo |

---

## O que foi feito em cada uma

### C-MONO — só recomposição, custo zero

Centro de massa em **x 74 % / y 53 %** → contrapeso à esquerda. A coluna `x 120–663` mede 17,4:1 de contraste com desvio 0,016.

- Bloco de mensagem movido para a coluna esquerda, alinhado à esquerda, centrado na altura do rosto (y 363–767).
- Largura travada em **543 px**: a silhueta dela começa em x 737 na faixa do bloco, o que dá 98 px de folga contra o piso de 80.
- Headline reescrito em 3 linhas para caber na coluna, mantendo os 72 px.
- **Data subiu para a faixa morta do topo** (y 96, energia 0,001). Liberou 110 px do bloco e criou dois níveis de informação.
- Subheads com quebra desenhada, sem palavra órfã.
- CTA alinhado ao mesmo eixo x=120.

### A-VERDE — reenquadramento

A lousa *parece* calma mas os feixes de sol estouram para `#8FB596`: texto branco daria **2,28:1**. Resolvido com recorte mais scrim local.

- `imageTransform` em CROP, `s=0,82 · tx=0,15 · ty=0`. Empurra a professora para baixo: o cabelo cai de y 350 para **y 427**.
- Escolha de `s` travada por duas restrições: cabelo ≥ 80 px abaixo do texto **e** manchete da tela do notebook (y 1024–1098) acima do topo do CTA (1154). Fora da janela 0,80–0,86 uma das duas quebra.
- Texto para o topo, sobre a lousa, eixo único à esquerda em x=120.
- `SCRIM-BASE` (1080×870 na base) virou `SCRIM-TOPO` 1080×660, duas paradas, `#0c1410` 0,94 → 0. Matiz da cena, sem escurecimento global.
- CTA fechado para `#0c1410@0,78 + #FFFFFF@0,05`: a barra de vidro a 0,35 caía sobre a tampa prateada do notebook e media **3,06:1**. É o caso que o sistema já prevê — faixa mais fechada quando o fundo é claro ou movimentado.

### B-MESA — imagem nova (75 créditos)

A única que precisou de pixel novo, e a medição é que decidiu: com desvio de 0,09–0,14 em toda a foto, o piso vira 7:1 e **nenhuma faixa passava**. Não era problema de layout.

Dois defeitos além do contraste, achados no caminho:
- **Objeto errado.** `vocabulario-visual.md` é explícito: produto digital pede objeto digital. Caderno de papel conta a história errada.
- **Não lia como professora.** Mãos escrevendo num caderno lê como "alguém fazendo diário", não como preparação de aula.

Cena nova (`assets/cena-professora-mesa-janela.png`): mesa de professora contra janela de cortina difusa, notebook com a página do curso em PT-BR, provas corrigidas a caneta vermelha, giz, apagador de lousa, óculos. Sem pessoas.

- **Não** foi pedida superfície lisa para segurar tipografia — proibido desde 2026-08-04. O campo homogêneo é a **janela difusa**, que é fenômeno de luz, não tampo fabricado.
- Contraste da tinta escura passou de 5,09:1 (melhor caso da foto velha) para **13,7:1**.
- Centro de massa em y 63 % → contrapeso no topo, exatamente onde o texto foi.
- CROP `s=0,83 · tx=0,085 · ty=0,17` para fechar o vazio de 300 px que abriu entre o texto e os objetos na primeira montagem.
- Headline subiu de 58 para 72 px, aproveitando o campo limpo.

---

## Auditoria final — contraste no pior caso, medido na chapa de fundo

Piso: 3:1 para texto grande, 4,5:1 para corpo, **7:1 quando o desvio do fundo passa de 0,08**.

| | A-VERDE | B-MESA | C-MONO |
|---|---|---|---|
| Chapéu | 12,62:1 | 4,95:1 | 10,11:1 |
| Headline neutro | 9,16:1 | 13,70:1 | 18,19:1 |
| Headline acento | 11,67:1 | 5,01:1 | 9,90:1 |
| Quadro | 6,90:1 | 13,72:1 | 18,59:1 |
| Decorado | 5,45:1 | 13,73:1 | 19,05:1 |
| CTA | 9,23:1 | 7,91:1 | 19,82:1 |

Todos passam. O mais apertado é o Decorado da A-VERDE a 5,45:1 (36 px Bold = texto grande, piso 3:1, desvio 0,049).

Piso tipográfico corrigido de 34 para **36 px** nas três — estavam abaixo do mínimo da skill.

### Distinção visual (Meta Ads Andromeda)

| Peça | Matiz | Sat | L médio |
|---|---|---|---|
| A-VERDE | 61,7° | 0,215 | 0,182 |
| B-MESA | 31,2° | 0,136 | 0,604 |
| C-MONO | 188,0° | 0,419 | 0,036 |

| Par | ΔMatiz | ΔL | Veredito |
|---|---|---|---|
| A × B | 30,5° | 0,423 | distintas |
| A × C | 126,4° | 0,146 | distintas |
| B × C | 156,8° | 0,568 | distintas |

Reprova exige ΔMatiz < 20° **somado a** ΔL < 0,05. Nenhum par chega perto.

**Atualização do registro de distinção:** a peça 4 deixou de ser "top-down flat lay, só mãos" e passou a ser **still-life sem pessoas, câmera à altura da mesa, contraluz difuso**. O lever "tinta escura sobre claro" continua sendo só dela.

---

## Aprendizado de método — como medir contraste sem número falso

Três medições deram falso durante esta refação. Vale registrar, porque vão se repetir:

1. **Caixa apertada e cheia de texto contamina o fundo.** O antialiasing das letras não é tinta nem fundo, e entra na amostra. O Decorado da A-VERDE mediu 4,59:1 na peça composta e **16,30:1** quando o fundo foi amostrado numa região sem texto na mesma altura.
2. **Caixa com duas cores de tinta dá número falso.** A segunda cor entra como se fosse fundo. Uma caixa por linha e por cor, e `--tinta` com o token que você mesmo aplicou.
3. **Esconder o texto para exportar a chapa move o CTA.** A barra tem auto-layout centralizado: sem o texto, o chip colorido reflui para o meio e cai dentro da caixa de medição. Meça o CTA **na peça final**, num pedaço da barra à direita do fim do texto.

O jeito confiável: chapa de fundo com **só os nós de TEXT ocultos** (a barra e o chip continuam visíveis), e caixas de medição conferidas contra a geometria real lida do Figma.

---

## Entregáveis

- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-05-spp-professora-AD-PROF-A-VERDE-1080x1350.png`
- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-05-spp-professora-AD-PROF-B-MESA-1080x1350.png`
- `produtos/seu-produto-pronto-com-ia/criativos/2026-08-05-spp-professora-AD-PROF-C-MONO-1080x1350.png`
- Cena nova em `assets/cena-professora-mesa-janela.png`

## Pendência no arquivo

`2662:1057` é um **duplicado antigo** de A-VERDE, empilhado nas mesmas coordenadas do original. Não foi tocado. Vale apagar depois de conferir que ninguém o referencia.
