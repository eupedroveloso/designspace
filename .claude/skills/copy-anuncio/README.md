# Skill copy-anuncio. Como instalar

Skill autossuficiente de criação de anúncios pela Mandala de 18 Tipos (metodologia VTSD).
Não depende de nenhum outro arquivo do projeto onde for instalada.

## Instalação

Descompacte e coloque a pasta `copy-anuncio` inteira dentro de `.claude/skills/` do projeto de destino:

```
seu-projeto/
└── .claude/
    └── skills/
        └── copy-anuncio/
            ├── SKILL.md
            └── references/
```

Se a pasta `.claude/skills/` ainda não existir, crie.

Para deixar a skill disponível em todos os seus projetos, coloque em `~/.claude/skills/copy-anuncio/`.

## Como usar

Abra o Claude Code no projeto e digite:

```
/copy-anuncio
```

Ou peça em linguagem natural: "quero criar anúncios para o meu produto".

## O que tem dentro

| Arquivo | O que é |
|---|---|
| `SKILL.md` | O fluxo completo em 8 passos. Ponto de entrada |
| `references/manual-copy.md` | Manual da Copy. 15 princípios, 20 vícios proibidos e o checklist final A/B/C/D |
| `references/checklist-light-copy.md` | As 12 proibições absolutas do Light Copy |
| `references/mandala-18-tipos.md` | Os 18 tipos, 4 objetivos, 3 momentos de consumo, CTAs e estrutura de campanha |
| `references/elementos-literarios.md` | Os 26 elementos literários. Aplicar de 1 a 3 por peça |
| `references/formatos-meta-ads.md` | Dimensões e limites de caractere do Meta |
| `references/formatos-google-ads.md` | Limites de títulos, descrições e negativas do Google |
| `references/formatos-virais-instagram.md` | Estruturas de retenção para vídeo curto |
| `references/exemplos-criativos.md` | Referências de peça pronta |
| `references/exemplos-leads-4-categorias.md` | 12 leads reais nas 4 categorias, em 3 nichos. Calibração de especificidade |

## Como ela se adapta ao projeto de destino

A skill procura um briefing de produto nesta ordem:

1. `meus-produtos/.ativo` e o `perfil.md` correspondente (padrão do Workshop Marketing IA)
2. `perfil.md`, `produto.md` ou `briefing.md` na raiz
3. `docs/` ou `briefing/`

Se não achar nada, ela faz uma entrevista curta de 4 perguntas (nicho, público, Quadro e preço) e segue normalmente. Funciona em projeto vazio.

Os arquivos gerados vão para a primeira pasta que existir entre `meus-produtos/{ativo}/entregas/criativos/`, `entregas/anuncios/` ou `anuncios/`.

## O que ficou de fora

A versão original no projeto Workshop Marketing IA aciona a skill `criativo-estatico` e o script `scripts/generate-creative.py` para gerar as imagens automaticamente via API (Freepik e HeyGen). Isso exige Python e chaves de API, então ficou fora deste pacote.

No lugar, o passo 7 gera o prompt visual pronto para colar na ferramenta que você escolher, com a sintaxe correta para cada uma das 11 IAs suportadas.
