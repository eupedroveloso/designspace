# Vocabulário visual — os objetos do produto digital

O SPP ensina profissional a transformar conhecimento em produto digital. A cena sozinha mostra só a **origem**: a dermatologista na maca, o advogado no escritório, a professora na sala. Falta o **destino**. Os objetos deste vocabulário são a evidência física da transformação, e é por isso que entram na peça.

Sem eles a peça é retrato de gente cansada. Com eles é retrato de gente cansada **que tem uma saída**.

---

## Princípio

**O objeto é prova, não enfeite.** Cada elemento responde "o que exatamente vira produto no caso desta pessoa". Ebook genérico flutuando não diz nada; um protocolo de pós-procedimento na mão de uma dermatologista diz tudo.

Isso significa que o objeto **muda por nicho**. Não existe kit fixo que se cola em qualquer peça:

| Nicho | O que o conhecimento dele vira |
|---|---|
| Dermatologia | protocolo de pós-procedimento, rotina de skincare, guia do paciente |
| Advocacia | modelo de petição, checklist de compliance, mentoria em vídeo |
| Nutrição | plano alimentar, receituário, curso de reeducação |
| Educação | apostila, videoaula, banco de exercícios |
| Estética | protocolo de cabine, precificação, curso de técnica |

---

## Biblioteca de ativos reais — use antes de construir qualquer coisa

**Elemento de plataforma nunca é remontado à mão.** Card de notificação inventado, ícone aproximado e "ebook" sem capa foram reprovados em 2026-08-03 por parecerem placeholder. Antes de desenhar qualquer objeto, olhe o que já existe:

| Ativo | Onde |
|---|---|
| Notificação de venda da Hotmart (SVG e PNG, vetorial, oficial) | `assets/hotmart/notificacao-venda.svg` |
| Logo Hotmart e chama isolada, cores oficiais `#F04E23` e `#093D4D` | `assets/hotmart/` (ver README de lá) |
| Livreto frontal recortado, capa em branco para receber design | `assets/ebook-livreto-frontal-recorte.png` |

Faltou o ativo de alguma plataforma? **Peça ao usuário** em vez de aproximar. Ele tem os arquivos e responde rápido, e uma marca redesenhada de memória sai errada e denuncia a peça.

## Catálogo de objetos

**O produto é digital, então o objeto é digital.** Livreto impresso, apostila e papel contam a história errada: o SPP ensina a criar produto **digital**, e o objeto na cena tem que remeter a isso. Tela de tablet, celular, notebook, player de aula. Papel só quando o produto realmente for físico.

| Objeto | O que comunica | Como entra |
|---|---|---|
| **Tablet com o guia na tela** | o produto existe e é digital | na cena, na mão da pessoa; **o texto da tela vem no prompt**, em PT-BR |
| **Celular com a aula ou o checkout** | o produto circula no bolso do cliente | idem |
| **Notebook com a página de vendas** | existe um lugar onde se compra | idem |
| **Notificação de venda da Hotmart** | vende sem a pessoa na sala | vetor oficial de `assets/hotmart/`, **em cascata de 3**, ver abaixo |
| **Ebook impresso** | só quando o entregável for mesmo físico | na cena, capa impressa pelo prompt |

---

## Notificação de venda: cascata, não unidade

Uma notificação sozinha diz "vendeu uma vez". **Três empilhadas dizem "vende sem parar"**, que é a promessa do produto. Foi assim que o usuário resolveu em 2026-08-03.

Parâmetros medidos da versão aprovada:

```
3 cópias do ativo oficial, 257×44 cada
empilhadas com gap 51, mesma coluna
opacidade decrescente de cima para baixo (a de baixo quase sumindo)
posicionadas na área livre ao lado do corpo do sujeito, sobre a foto
escala pequena: o texto delas é textura, não mensagem
```

Escala pequena é decisão, não descuido: a notificação é **contexto**, não copy. Quem precisa ler o valor não é o usuário do feed. Por isso ela pode ficar abaixo do piso de 36 px sem ser achado, desde que a copy do anúncio não dependa dela.

## Regras duras

**0. O objeto nasce DENTRO da cena, não é colado depois.**
Recortar um objeto e pousar por cima da foto, com sombrinha embaixo, produz peça de adesivo. Foi assim que a primeira versão da peça de dermatologia foi reprovada. O objeto físico entra **no prompt da cena**: na mão da pessoa, sobre a mesa dela, apoiado no móvel, com a luz e a sombra de contato que a própria fotografia produz. Peça a capa **em branco** no prompt, e o título vai por cima como vetor no Figma.

Só permanece como recorte flutuante o que é **interface**, porque interface não existe fisicamente na sala: notificação, checkout, gráfico. E mesmo esses se ancoram à margem do grid, compartilhando o eixo com o bloco de texto, em vez de boiar em qualquer lugar da foto.

**0.1. Reserve o espaço do texto ANTES de gerar a cena.**
O bloco tipográfico ocupa de 350 a 400 px de um canvas de 1350, mais a barra de CTA. Isso significa que **sujeito e objetos precisam caber acima de y≈800**. Diga isso no prompt de forma literal ("her head, her hands and the booklet all sit inside the upper 55 percent of the frame; the lower 45 percent is empty floor"), e confira antes de montar. Gerar uma cena bonita e descobrir depois que o objeto caiu na faixa do texto custa uma geração inteira, e foi o que aconteceu duas vezes aqui.

Efeito colateral conhecido: pedir a divisão de forma literal pode fazer o modelo criar uma **emenda horizontal** entre a cena e a área vazia. Posicione o topo do scrim exatamente nessa linha e ela desaparece.

**1. Texto de objeto nasce na imagem. Só Head, SubHead e CTA são vetor.**
Corrigido em 2026-08-03, e o que estava escrito aqui antes estava errado. Se o objeto precisa carregar texto (tela de tablet, capa, embalagem), **peça esse texto no prompt da imagem, em PT-BR**, descrevendo exatamente o que aparece. Sobrepor texto vetorial a um objeto fotografado não funciona: o Figma não faz perspectiva, não interage com a luz da cena nem com a textura da superfície, e o resultado parece adesivo. Ou o texto vem na imagem, ou o objeto fica sem texto.

A única exceção são elementos que **são interface pura e chegam prontos como vetor**, tipo a notificação oficial da Hotmart em `assets/hotmart/`. Ali o vetor é o ativo real, não uma imitação de superfície.

**2. Gere o objeto separado da cena.**
Um prompt só, pedindo cena e objeto juntos, entrega objeto deformado. Gere isolado, em fundo cinza chapado, e recorte com `images_remove_background`. Vale a mesma instrução da `anatomia.md` para o asterisco da marca.

**3. A luz do objeto obedece a luz da cena.**
Antes de escrever o prompt do objeto, olhe de onde vem a chave na foto de fundo. Se a cena tem janela à esquerda, o objeto é iluminado pela esquerda e a sombra de contato cai para a direita. Objeto com luz contrária é o que mais denuncia colagem.

**4. Dois a três objetos, nunca mais.**
Eles vivem no **plano do meio** (ver `legibilidade-e-densidade.md`), entre o sujeito e o texto. Escalas diferentes entre si, sobreposição leve, rotação de 3° a 8°. Quatro ou mais viram vitrine e a peça perde o foco único que quebra a cegueira de banner.

**4.1. Ebook sem capa não é ebook.**
Livreto de capa em branco lê como maquete inacabada. Todo objeto impresso recebe **capa de verdade**: título do produto, subtítulo que explica a entrega, régua ou marca de apoio, na paleta do nicho e não na da marca do evento. A capa é vetor no Figma sobre a foto do objeto, então gere o objeto **frontal**, sem perspectiva, para o vetor encaixar sem distorção. Dimensione o objeto para que o título da capa não caia abaixo de ~25 px.

**5. Nunca invente número de faturamento.**
Card de venda mostra que **houve** venda, com o nome do produto. Não inventa valor, não inventa quantidade, não simula extrato. Prova fabricada é problema jurídico e de reputação, não licença criativa. Se o cliente tiver print real com autorização de uso, aí sim entra o valor.

**6. Logo de terceiro só com o arquivo oficial.**
Hotmart, Zoom, WhatsApp e afins entram apenas quando o usuário fornecer o SVG. Redesenhar marca de memória entrega aproximação errada e uso indevido. Sem o arquivo, use o card na gramática visual da plataforma (formato, raio, hierarquia) sem a marca.

**7. Objeto não invade texto.**
Vale a regra 3 da `regras-de-composicao.md`. O objeto ocupa a área da cena, acima da faixa de texto. Se não couber sem encostar, ele diminui ou sai; o texto não se aperta para caber objeto.

---

## Sombra de contato

Objeto recortado sem sombra flutua e denuncia colagem. Cada objeto recebe:

```
DROP_SHADOW  na cor da cena (efeitos #4), não em preto neutro
  radius 40–70   offset y 18–30   opacidade 0.35–0.55
  offset x seguindo a direção da luz da cena
```

Em objeto que "encosta" em algo, some uma segunda sombra fechada: `radius 8–14`, `y 4–8`, opacidade maior. É a que dá contato; a larga só dá volume.
