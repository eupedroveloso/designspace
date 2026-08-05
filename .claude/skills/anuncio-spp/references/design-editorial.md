# Design editorial — onde o texto mora na peça

Referência obrigatória, criada em **2026-08-05** a partir de três peças reprovadas pelo usuário no arquivo `Seu Produto Pronto`. Cada regra aqui nasceu de um erro medido, não de teoria.

| Peça | Erro | Número que reprova |
|---|---|---|
| `2662-1059` | texto empilhado no topo, mulher à direita, terço esquerdo morto | zona livre de **240×472** com energia 0,001 desperdiçada |
| `2662-1058` | texto escuro e laranja direto sobre bokeh claro | chapéu com **1,43:1** de contraste no pior caso |
| `2662-1093` | headline disputando espaço com a professora e o notebook | texto na faixa de **maior** desvio da peça (0,20), com o topo vazio |

> **A regra que resume as três:** o texto não tem lugar fixo. **A imagem decide onde o texto vai**, e isso se descobre medindo antes de escrever a primeira letra.

---

## 1. A ordem correta de trabalho

Errado — e foi o que produziu as três peças acima:

```
gera a imagem  →  joga o texto no topo  →  vê se dá pra ler  →  escurece a foto até dar
```

Certo:

```
gera a imagem
  →  MEDE a imagem: onde está a massa, onde está o vazio, qual a matiz
  →  ESCOLHE a zona de texto pelo contrapeso
  →  ENQUADRA a imagem para abrir aquela zona
  →  compõe o texto dentro dela
  →  MEDE o contraste no pior caso
```

A ferramenta que faz os dois "MEDE" está em `scripts/analise-composicao.py`:

```bash
python3 -m venv venv && ./venv/bin/pip install Pillow
./venv/bin/python .claude/skills/anuncio-spp/scripts/analise-composicao.py imagem.png
```

Ela devolve o mapa de energia, o centro de massa do assunto, o lado do contrapeso e o ranking de zonas livres. **Rode na imagem gerada, antes de montar no Figma.** Rodar na peça pronta faz o próprio texto entrar na conta como assunto e o centro de massa mente.

---

## 2. Contrapeso — o texto vai no lado oposto à massa

Foi a queixa exata na `2662-1059`: *"como a composição está mais horizontal você podia colocar o texto no lado oposto à imagem da mulher, texto à esquerda e imagem à direita."*

O assunto tem um centro de massa. O texto é a outra massa da peça. **Duas massas do mesmo lado desequilibram; massas opostas se sustentam.**

| Centro de massa do assunto | Onde o texto vai |
|---|---|
| Terço **direito** (x > 55 %) | bloco à **esquerda**, alinhado à esquerda |
| Terço **esquerdo** (x < 45 %) | bloco à **direita**, alinhado à direita |
| **Centralizado** (45–55 %) | bloco **acima ou abaixo**, centralizado — nunca ao lado |
| Assunto na **base** | texto no **topo**, e vice-versa |

O script já entrega essa leitura pronta na linha `CONTRAPESO`.

### O que aconteceu na 2662-1059

Medido na foto, ignorando a faixa de texto:

```
CENTRO DE MASSA   x 59 %  y 58 %   →  DIREITA / BASE
CONTRAPESO        texto à ESQUERDA

ZONA LIVRE #1     x 0–240  y 270–742   energia 0,001   luminância 0,003
```

Traduzindo para o canvas real de 1080×1350: uma faixa de **360 × 708 px** de preto absoluto, um terço da largura da peça, com energia praticamente nula — o melhor lugar possível para tipografia branca. Estava vazia. O texto foi para o topo, empilhado, em cima da parte mais movimentada.

**Regra dura:** se o script aponta uma zona livre com área ≥ 6 células e energia < 0,05, e o bloco de texto não está nela, a peça volta.

### Texto lateral não é texto pequeno

Bloco à esquerda com o assunto à direita **continua obedecendo o piso de 36 px** e a proporção 40/40/20. Coluna estreita não autoriza fonte menor — autoriza **menos palavras** e headline em mais linhas. A medida de linha ideal cai para 15–28 caracteres nesse formato, o que costuma melhorar o gancho em vez de piorar.

---

## 3. Eixo de alinhamento — um só, e ele existe na imagem

Alinhamento não é propriedade de parágrafo. É um **eixo vertical concreto** que atravessa a peça, e tudo se pendura nele.

**Regras:**

1. **Um eixo primário por peça.** Chapéu, headline, subhead e a borda do CTA compartilham o mesmo `x`. Dois eixos só quando um deles é claramente subordinado (uma data deslocada, um selo girado).
2. **O eixo conversa com a imagem.** O melhor `x` não é o da margem — é o de uma vertical que já existe na cena: a borda do corpo do sujeito, o batente de uma porta, a linha de uma parede, a borda de uma mesa. Quando o eixo do texto coincide com uma vertical da foto, a peça parece composta; quando não, parece texto colado.
3. **Alinhamento centralizado exige assunto centralizado.** Texto centralizado sobre assunto lateral é o desalinho mais comum e o mais fácil de evitar.
4. **Nunca justificado.** Rio de espaço em headline de anúncio é defeito.
5. **Alinhamento à direita só com assunto à esquerda**, e nunca em bloco com mais de três linhas — a entrada irregular da linha cansa.

### Alinhamento ótico, não métrico

O Figma alinha pela caixa; o olho alinha pela forma. Corrija à mão:

| Caractere na entrada da linha | Recuo negativo |
|---|---|
| Aspas `"` `"` | −0,22 em (~ −22 px num corpo de 100) |
| `O` `C` `G` `Q` `S` maiúsculos | −0,015 a −0,02 em |
| `A` `V` `W` `Y` | −0,02 em |
| `T` | −0,01 em |

Sem isso a primeira linha de um headline que começa com aspas parece recuada, e é o defeito que mais denuncia peça montada por quem não é designer.

---

## 4. Respiro — espaço é hierarquia, não sobra

Respiro não é "deixar um vão". É a **relação** entre vãos que informa o que é grupo e o que é nível.

### A escada de espaço

Dentro de um grupo o espaço é sempre menor que entre grupos, na proporção mínima de **1:2**:

```
entrelinha dentro do headline .......  0,88 a 0,95 × o corpo     (headline grande sempre < 1)
entrelinha do corpo .................  1,35 a 1,50 × o corpo
entre chapéu e headline .............  22 px          ← ritmo da casa
entre headline e subhead ............  22 px
entre subhead e CTA .................  ≥ 44 px        ← o dobro, marca o fim do bloco
margem do bloco à borda do frame ....  120 px         ← maior que qualquer vão interno
```

**Teste:** o maior vão *interno* do bloco tem que ser menor que a margem externa. Se o texto está a 60 px da borda e tem 80 px entre grupos, o bloco vaza — o olho lê os grupos como peças separadas e não como uma unidade.

### Respiro contra a imagem, não só contra a borda

O bloco de texto tem quatro vizinhos: as bordas do frame **e o assunto**. A distância mínima ao assunto é **maior** que à borda, porque o assunto tem detalhe e a borda não:

| Vizinho | Distância mínima |
|---|---|
| Borda do frame | 60 px (limite) · 120 px (bloco de texto) |
| Silhueta do sujeito | **80 px** |
| Objeto com detalhe alto (notebook, tela, mão) | **100 px** |
| Barra de CTA | 44 px |

Na `2662-1093` a headline ficou a menos de 20 px do braço da professora e a ~25 px da tampa do notebook. As duas coisas com detalhe, as duas brigando com a leitura.

### Respiro não se conquista encolhendo texto

Quando falta espaço, a ordem de solução é sempre esta, e nunca outra:

1. **Corte palavra.** Headline de anúncio vive com 4 a 8 palavras.
2. **Reenquadre a imagem** (seção 5).
3. **Mude a zona de texto** para outra zona livre do ranking.
4. **Corte uma linha inteira** de apoio.

Diminuir o corpo da fonte **não está na lista**. Já foi motivo de reprovação duas vezes.

---

## 5. Enquadramento — a foto se ajusta ao texto

Foi a queixa na `2662-1093`: *"você deveria ter enquadrado melhor a imagem, você deixou ela quase embaixo do texto sendo que tem um grande espaço disponível. As coisas não precisavam estar brigando pelo mesmo espaço."*

**A imagem dentro do frame é material, não é intocável.** O `imageTransform` em modo `CROP` desloca e escala a foto de graça, sem gerar de novo. Se o assunto está onde o texto precisa estar, **mova o assunto**.

### O que estava errado na 2662-1093

Faixas horizontais de 90 px, na peça de 720×900:

```
y   0–90    lum 0,054   desvio 0,099   ← lousa: a faixa MAIS CALMA da peça, vazia
y  90–180   lum 0,136   desvio 0,158
y 180–270   lum 0,196   desvio 0,179
...
y 540–630   lum 0,148   desvio 0,190   ← o headline foi para cá
y 630–720   lum 0,142   desvio 0,201   ← a faixa MAIS MOVIMENTADA da peça
```

O texto foi parar na faixa de maior desvio da peça inteira, colado no braço e no notebook, enquanto os 270 px de lousa no topo — a região mais calma e mais escura — ficaram sem função. A foto precisava descer, ou o crop precisava subir. Nenhum pixel novo era necessário.

### Protocolo de enquadramento

1. Escolha a zona de texto pelo contrapeso (seção 2).
2. Meça onde o assunto está agora.
3. Se ele invade a zona, ajuste nesta ordem:
   - **`imageTransform` em CROP** — desloca a foto no frame. Custo zero.
   - **Escala da foto** — até 1,25×. Acima disso perde nitidez em 1080×1350.
   - **`images_expand` no Magnific** — quando a foto não tem material suficiente do lado que você precisa abrir. É o certo quando a composição pede ar que a foto original não tem.
   - **Gerar de novo com a zona pedida no prompt** — último recurso, e o prompt pede *composição*, não superfície: `subject occupying the right two thirds, deep unlit shadow filling the left third` e nunca "mesa lisa na frente".
4. Meça de novo. A zona de texto precisa fechar com energia < 0,05.

### Vale para todo enquadramento

- **Nada de assunto cortado ao meio pela margem do texto.** Se o bloco de texto corta o sujeito na altura do rosto ou das mãos, reenquadre.
- **Olhar do sujeito aponta para dentro.** Pessoa olhando para fora da peça leva o olho embora. Se ela olha para a esquerda, o texto vai para a esquerda — o olhar vira seta apontando para a mensagem.
- **Espaço à frente, não atrás.** Sujeito de perfil precisa de mais ar do lado para onde olha. Esse ar é exatamente onde o texto mora.

---

## 6. Contraste — mede-se o pior caso, nunca a média

Foi a queixa na `2662-1058`: *"o contraste de cor do texto com o fundo ficou muito ruim... afinal nós dependemos dos leads lerem a mensagem, se você erra nisso nós temos prejuízo."*

### O defeito de método

A receita antiga mandava comparar a **luminância média** da região atrás do texto. Sobre fundo homogêneo isso funciona. Sobre bokeh, não: a média passa e o ponto pior reprova, e é o ponto pior que decide se a palavra some.

Medido na `2662-1058`:

| Faixa | Tinta | Fundo (p10 → p90) | Escuro | Médio | Claro | **Pior** |
|---|---|---|---|---|---|---|
| Chapéu "21 E 22 DE AGOSTO" | `#B23A0F` | `#997554` → `#E5BE95` | 1,43:1 | 2,63:1 | 3,46:1 | **1,43:1** |
| Headline | `#2A1D12` | `#AA896D` → `#DDBB95` | 5,07:1 | 7,05:1 | 9,05:1 | **5,07:1** |
| Subhead | `#2A1D12` | `#A37E61` → `#DFC5A4` | 4,45:1 | 5,75:1 | 9,87:1 | **4,45:1** |

O chapéu laranja não alcança 4,5:1 **em nenhum** dos três níveis — nem no melhor. Laranja `#B23A0F` sobre bokeh âmbar é laranja sobre laranja: matiz próxima e luminância próxima. Estava ilegível no feed, e o subhead a 4,45:1 reprova o piso de corpo.

### O critério novo

```
contraste = min(tinta × fundo_p10, tinta × fundo_p50, tinta × fundo_p90)
```

| Texto | Mínimo do PIOR caso |
|---|---|
| Corpo, apoio, chapéu, data | **4,5:1** |
| Texto grande (≥ 30 px normal, ≥ 24 px bold) | **3:1** |
| Sobre fundo com desvio > 0,08 | **7:1** — fundo movimentado exige folga |

O comando:

```bash
./venv/bin/python .claude/skills/anuncio-spp/scripts/analise-composicao.py peca.png \
  --tinta B23A0F --texto 128,102,596,126 \
  --tinta 2A1D12 --texto 105,232,618,258
```

Uma caixa por linha e por cor. Caixa com duas cores de texto dentro produz número falso — o script avisa quando detecta, mas passar `--tinta` com o token que você mesmo aplicou é sempre o número confiável.

### Três jeitos de medir errado

Aprendidos na refação de 2026-08-05, os três geraram número falso e todos vão se repetir:

1. **Caixa apertada e cheia de texto contamina o fundo.** O antialiasing das letras não é tinta nem fundo, e entra na amostra puxando o resultado para baixo. O Decorado da `2662:1093` mediu **4,59:1** na peça composta e **16,30:1** quando o fundo foi amostrado numa região sem texto, na mesma altura. Diferença de 3,5×.
2. **Caixa com duas cores de tinta.** A segunda cor entra como se fosse fundo e derruba o pior caso para ~1,4:1. Sempre uma linha e uma cor por caixa.
3. **Esconder o texto para exportar a chapa move os elementos com auto-layout.** A barra de CTA centraliza o conteúdo: sem o nó de texto, o chip colorido reflui para o meio da barra e cai dentro da caixa de medição. Resultado: as três peças "reprovaram" o CTA por artefato.

**O jeito confiável:**

```
1. Esconda SÓ os nós do tipo TEXT. Barra de CTA, chip e ícone continuam visíveis.
2. Exporte a chapa de fundo pela API REST.
3. Leia a geometria real de cada nó no Figma (absoluteBoundingBox) e use essas
   coordenadas como caixa de medição — nunca coordenadas estimadas do screenshot.
4. Meça o texto do CTA na PEÇA FINAL, num pedaço da barra à direita do fim do
   texto, porque a chapa não representa a barra depois do reflow.
```

Quando um número parecer estranho, recorte a região e **olhe** antes de corrigir a peça. Duas das três "reprovações" desta rodada eram defeito da medição, não do design — e corrigir a peça teria piorado o que já estava certo.

### Cor de acento nunca escapa da medição

O erro da `2662-1058` foi assumir que a cor de acento "aparece porque é vibrante". Saturação não é contraste. **Acento quente sobre cena quente é o caso mais perigoso**, porque a matiz próxima engana o olho de quem está desenhando com a peça a 100 % de zoom — e o lead vê a 37 %.

Se o acento não passa no pior caso, as saídas, nesta ordem:

1. **Muda a zona de texto** — outra região da imagem resolve de graça.
2. **Escurece o acento** até passar, mantendo a matiz. Laranja de acento em cena clara vira `#7A2A08`, não deixa de ser laranja.
3. **Inverte:** tinta escura da matiz da cena, sem halo.
4. **Scrim local de duas paradas**, na matiz da cena, só na faixa do texto. Nunca escurecimento global.

Halo claro atrás de texto escuro continua **proibido** — deixa a peça com cara falsa.

---

## 7. Equilíbrio ótico

- **O centro ótico fica ~5 % acima do centro geométrico.** Bloco de texto centralizado verticalmente por número parece baixo. Suba.
- **Massa escura pesa mais que massa clara** de mesma área. Uma silhueta preta à direita precisa de mais texto à esquerda para equilibrar do que uma área clara equivalente.
- **Margem ótica na base é maior.** Em peça com CTA ancorado, a margem inferior visual precisa ser 10–15 % maior que a lateral, ou a peça parece escorregando.
- **Meça a mancha, não confie no olho.** A regra da palavra-herói em `regras-de-composicao.md` §7 continua valendo: a largura da mancha da palavra que carrega a ideia é ≥ a da linha acima dela.

---

## 8. Medida de linha

| Nível | Caracteres por linha | Linhas máximas |
|---|---|---|
| Headline | 18 – 34 | 3 |
| Headline em coluna lateral | 15 – 28 | 4 |
| Subhead / apoio | 34 – 52 | 3 |
| CTA | 26 – 42 | 2 |

Acima do teto o olho perde a linha de retorno. Abaixo do piso o texto vira escada e a mancha fica esfarrapada.

---

## 9. Checklist antes de fechar

Cada item é numérico. Reprova sem discussão.

```
□ Rodei analise-composicao.py na IMAGEM, antes de montar
□ O bloco de texto está no lado do CONTRAPESO apontado pelo script
□ A zona escolhida tem energia < 0,05
□ Não sobrou zona livre ≥ 6 células fora de uso
□ Um único eixo de alinhamento, e ele coincide com uma vertical da cena
□ Alinhamento ótico corrigido em aspas e redondas
□ Vão interno máximo < margem externa
□ ≥ 80 px entre o texto e a silhueta do sujeito · ≥ 100 px de objeto detalhado
□ Contraste do PIOR CASO ≥ 4,5:1 (corpo) e ≥ 3:1 (texto grande)
□ Fundo com desvio > 0,08 sob o texto → contraste ≥ 7:1 ou scrim local
□ A cor de acento foi medida, não presumida
□ Nenhum texto abaixo de 36 px
□ Simulei a 400 px de largura e li tudo
```
