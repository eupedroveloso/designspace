---
name: design-replica
description: Replica um design de referência no Figma com fidelidade pixel a pixel — extrai cor, posição, tipografia e efeito por medição real da imagem, separa o que é Magnific e o que é vetor Figma, e reconstrói com todo texto editável. Use quando o usuário envia uma imagem e pede para recriar, espelhar, refazer ou adaptar aquele design no Figma.
---

# Réplica de design

Objetivo: sair de uma imagem de referência para um arquivo Figma editável que, sobreposto à referência, coincide.

**Estimar a olho é o erro que define o resultado.** Nenhuma cor, coordenada ou tamanho entra no Figma sem ter sido medido. Este é o ponto inteiro da skill.

---

## 0. Onde a réplica nasce

Pergunte ao usuário o link do arquivo Figma de destino — com página e seção, se ele souber — e registre com `/figma-destino`. Vale mesmo quando o original está no Figma: **o arquivo que você lê para medir não é, por padrão, o arquivo onde você escreve.** Um hook bloqueia a escrita enquanto não houver destino registrado.

---

## 1. Medir antes de qualquer coisa

Trabalhe sobre o arquivo real da imagem, não sobre a impressão visual dela.

Ambiente: Pillow não vem no Python do sistema. Crie um venv no scratchpad uma única vez.

```bash
python3 -m venv venv && ./venv/bin/pip install --quiet Pillow
```

Extraia, nesta ordem:

**Dimensão do canvas.** `im.size`. Todo o resto é relativo a isso.

**Fundo.** Amostre os 4 cantos, o centro e os pontos médios das bordas. Diferença entre centro e cantos revela gradiente radial. Diferença entre lados revela gradiente linear. Igualdade revela cor chapada.

**Bounding box de cada elemento.** Máscara por predicado de cor, varrendo a região. Devolve `(x0, y0, x1, y1)` real.

```python
def bbox(pred, x0, y0, x1, y1):
    xs, ys = [], []
    for y in range(y0, y1):
        for x in range(x0, x1):
            if pred(px[x, y]): xs.append(x); ys.append(y)
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None
```

Cuidado com predicados largos: tom de pele passa em quase todo teste de "laranja" e contamina o bbox. Aperte o predicado e restrinja a janela de busca até o resultado bater com o que você vê.

**Gradientes.** Amostre ao longo do eixo, de ponta a ponta. Duas paradas raramente descrevem o gradiente real — colete 4 a 6 pontos e veja se a interpolação é linear.

**Transparência e blur.** Compare o mesmo x acima e dentro da região suspeita. Se a razão entre as diferenças de canal não for consistente, não é alpha simples: é frosted glass (alpha + background blur).

**Confirme visualmente.** Recorte as regiões ambíguas, amplie 2-3× com LANCZOS e olhe. Medição diz o valor; o recorte diz o que a coisa é. Um bbox laranja pode ser um objeto 3D, um brilho desfocado ou um braço.

---

## 2. Identificar tipografia

Recorte cada bloco de texto e amplie. Olhe as marcas que distinguem famílias:

- Ápice do A: plano, pontudo ou cortado
- Terminais do C e do S: horizontais ou angulados
- g de um ou dois andares
- Largura do O: circular (geométrica) ou oval (grotesca)
- Inclinação real do itálico, se houver

Registre a família provável e **duas alternativas** disponíveis no Figma. Se a fonte exata não existir, escolha a mais próxima e **declare a substituição na entrega**. Nunca finja que casou.

Meça também: altura de caixa alta em px, tracking aparente, entrelinha entre linhas de um mesmo bloco.

---

## 3. Separar Magnific × Figma

Escreva a divisão antes de construir. Ela governa todo o resto.

| Vai para o **Magnific** | Vai para o **Figma** |
|---|---|
| Fotografia, pessoas, produtos | **Todo texto, sem exceção** |
| Cena, textura, atmosfera | Formas geométricas e vetoriais |
| Objeto com material complexo ou orgânico | Gradientes, barras, pills, ícones |
| O que precisa parecer fotografado | O que precisa de borda limpa ou de ser editável |

Na dúvida, **Figma**. Vetor é nítido em qualquer zoom, editável e não custa crédito. Forma geométrica limpa pedida a modelo de imagem volta borrada e assimétrica.

**Nunca peça texto ao modelo de imagem.** Todo prompt de fundo termina com `no text, no numbers, no readable characters, no logos`.

Para a foto: descreva a cena com a precisão que a referência mostra (roupa, cor, pose, enquadramento, luz, lente) e gere com fundo neutro para remover depois com `images_remove_background`.

---

## 4. Construir

De trás para frente: fundo → decorativos → imagem → overlays → texto.

Antes de escrever, carregue `/figma-use`. Delegue ao `figma-master`.

- Frame na dimensão exata medida, `clipsContent` ligado
- Cada elemento na coordenada medida, não na aproximada
- Texto sempre camada de texto, nomeada por função, com size/weight/tracking/line-height explícitos
- Gradiente de texto via fill `GRADIENT_LINEAR` no próprio nó de texto, mantendo editável
- Frosted glass via fill semi-transparente + `BACKGROUND_BLUR`
- Decorativo desfocado via vetor + `LAYER_BLUR`, mantendo o vetor
- Elemento que sangra na borda entra inteiro e é cortado pelo frame, nunca desenhado pela metade

---

## 5. Conferir por sobreposição

`get_screenshot` do frame. Compare com a referência **elemento a elemento**, não pela impressão geral.

Confira nesta ordem, que é a ordem em que o erro aparece: posição vertical dos blocos de texto → largura do bloco de texto (revela erro de font-size) → paradas de gradiente → raio de canto → opacidade e blur.

Achou desvio, corrija e tire novo screenshot. Repita até coincidir. **Desvio acumulado vira retrabalho**, então corrija na etapa em que apareceu.

Se quiser medir em vez de olhar, exporte o screenshot e rode a mesma extração de bbox nos dois arquivos — a diferença numérica é o desvio real.

---

## 6. Entregar

- Link do frame
- A divisão Magnific × Figma que você aplicou
- Desvios conhecidos, com motivo: fonte indisponível, foto não idêntica por ser regeneração, limitação da API
- Confirmação de que todo texto está editável

**Nunca declare fidelidade que não conferiu por screenshot.** A regeneração da foto nunca é idêntica ao original — diga isso na entrega em vez de deixar o usuário descobrir.
