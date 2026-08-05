---
name: leandro-ladeira
description: Gera a imagem de anúncio com o rosto real do Leandro Ladeira, usando as fotos de referência de assets/leandro-ladeira/ no Magnific, mais a direção visual do personagem. Use SEMPRE que o pedido envolver o rosto dele, "com o Leandro", "com o Ladeira", "foto do expert", "anúncio de autoridade", "o protagonista da marca", ou quando a peça for do sistema Seu Produto Pronto com IA e a cena tiver uma pessoa. Nunca gere o rosto dele de memória nem por personagem de biblioteca.
---

# Rosto do Leandro Ladeira

O rosto dele é ativo de marca. **Nunca é gerado de memória, nunca sai de personagem de biblioteca do Magnific.** Toda imagem com ele passa pelas fotos de referência que moram em `assets/leandro-ladeira/`, por decisão do usuário.

Esta skill resolve **a pessoa e a direção do personagem**. Ela não decide layout, não decide copy e não substitui nada:

- Cena, luz, paleta e textura continuam vindo de `/ref-ads-dna`
- Copy continua vindo de `/copy-anuncio` ou `/copy-card`, filtrada pela `revisora`
- Grid, tokens e camadas da marca continuam em `/anuncio-spp`
- Formato continua sendo o do projeto: **uma peça, 1080×1350, `imagen-nano-banana-2`**

---

## 1. Recuperar as referências no Magnific

Leia `assets/leandro-ladeira/magnific-ids.md`. As creations persistem na conta, então na maioria das sessões não há upload nenhum a fazer.

| Arquivo local | Identifier |
|---|---|
| `15.jpg` (estúdio, fundo de grade com lâmpadas) | `rgLEksjxtc` |
| `freepik__...4754.png` (fundo branco) | `s7SHjUjl8e` |

Se uma geração falhar por creation inexistente, suba de novo com `creations_upload_show` (o servidor não lê arquivo do host direto) e **atualize a tabela do `magnific-ids.md` com a data**. Em execução headless, o caminho é `creations_request_upload` → PUT dos bytes na URL presignada com `curl.exe` via PowerShell → `creations_finalize_upload` com `visible: false`. Use `curl.exe`, não o Bash desta máquina, que engole a saída do upload.

Passe **todas** as referências disponíveis na geração:

```
references: [
  { type: "image", identifier: "rgLEksjxtc" },
  { type: "image", identifier: "s7SHjUjl8e" }
]
```

No prompt, o sujeito é descrito como **"the man from the reference images"**.

---

## 2. O que a referência trava, e o que ela não trava

**Trava só a pessoa: rosto, cabelo, barba.**

**Não trava figurino nem cenário.** Roupa e ambiente são inventados do zero, conforme o conceito do anúncio. Se o prompt repetir a camiseta ou o fundo das fotos de referência, está errado: é sinal de que você descreveu a foto em vez de descrever a cena.

**Exceção de marca:** em peça do sistema `/anuncio-spp`, a camiseta petróleo/teal é invariante da marca (invariante nº 1 daquela skill) e entra no prompt por decisão de identidade, não por cópia da referência. Fora do SPP, o figurino é livre e muda a cada peça, porque figurino repetido é uma das alavancas que fazem duas peças parecerem irmãs no feed.

---

## 3. Direção visual do personagem

Ele não é infoprodutor padrão nem sábio corporativo. O retrato é **humano, descontraído e comporta humor**: expressão espontânea, gente real, camiseta, ambiente vivido, luz quente, comicidade na cena quando a copy pedir.

**Toda cena dele exige uma ação ou situação concreta.** Ele está segurando algo, no meio de algo, reagindo a algo. "Homem em pé posando" volta na auditoria.

Proibido, sem exceção:

- Pose de palestrante, microfone de headset, palco corporativo
- Terno, camisa social, camisa abotoada
- Braços cruzados de capa de revista
- Retrato parado, sem situação nenhuma em volta
- Escritório executivo impessoal, parede de vidro, cadeira de couro
- Sorriso de banco de imagem

**Olhar para a câmera é bem-vindo, parado não.** A regra de leitura imediata do `CLAUDE.md` diz que rosto humano com emoção legível olhando para a lente é o que mais atravessa a cegueira de banner, e isso continua valendo aqui. O que está proibido é o retrato **sem situação**: ele pode olhar para a câmera desde que esteja no meio de alguma coisa, e a expressão precisa ser legível a 37 % do tamanho.

---

## 4. Conferência antes de montar

Baixe a prévia e confira, nesta ordem, antes de gastar tempo no Figma:

1. **Semelhança do rosto.** Derivou, regere. Rosto parecido não serve: é o rosto da marca.
2. **Ação presente na cena.** Se você não consegue dizer o que ele está fazendo em uma frase, a cena está errada.
3. **Figurino e cenário não copiados da referência.**
4. **Nada de logo de terceiro, texto ilegível ou mão distorcida.**
5. **Zona livre para o texto** existe onde o contrapeso pede. Meça com `.claude/skills/anuncio-spp/scripts/analise-composicao.py` antes de decidir onde a headline mora.

Você escolhe a variação, não o usuário. Diga em uma linha o que descartou e por quê.

---

## 5. Registro

Ao fechar a peça, anote em `outputs/` qual foi o figurino, o cenário e a chave de luz usados com ele. É o que impede a próxima peça de repetir a mesma combinação, que é exigência da regra de distinção visual do `CLAUDE.md`.
