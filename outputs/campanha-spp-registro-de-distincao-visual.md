# Campanha SPP — registro de distinção visual

Exigência do **Meta Ads Andromeda**: os criativos do conjunto precisam parecer visualmente diferentes. Este arquivo existe para a próxima peça **não repetir** combinação já usada. Consulte antes de escolher a direção de arte.

## Combinações já usadas

| # | Nicho | Matiz | Sat | L médio | Chave de luz | Ângulo | Tipografia | Texto | Direção de arte |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dermatologia | **26,0°** | 0,334 | 0,136 | low-key | altura dos olhos, plano médio | Albert Sans | branco sobre scrim escuro | retrato em pé, tablet na mão |
| 2 | Professores | **201,9°** | 0,060 | 0,615 | high-key difusa | baixo, plano geral | Exo 2 + Inter | tinta escura com halo | sala vazia, sujeito lateral |
| 3 | Professores | **61,7°** | 0,215 | 0,182 | **sol duro, sombra recortada** | **plongée** | **Anton** | branco sobre scrim de topo, **alinhado à esquerda** | quadro-verde, sujeito visto de cima |
| 4 | Professores | **31,2°** | 0,136 | 0,604 | **contraluz difuso de janela**, high-key | altura da mesa, 50 mm | **Manrope** | **tinta escura sobre campo claro, sem halo** | **still-life sem pessoas**, mesa de professora |
| 5 | Professores | **188,0°** | 0,419 | 0,036 | **low-key, luz de tela** | 85 mm, retrato fechado | Albert Sans Black caixa alta | branco sobre preto natural | retrato noturno, **texto em coluna à esquerda** |

> **Perfis 3, 4 e 5 remedidos em 2026-08-05**, depois da refação das três peças de professores. Os valores antigos (79,2° / 359,6° / 14,4°) descreviam versões que não existem mais — a 4 ganhou cena nova e as três mudaram enquadramento, scrim e posição do texto. Registro completo em `2026-08-05-spp-professora-refacao-editorial.md`.
>
> Distâncias entre as três, conferidas: A×B **30,5° e 0,423** · A×C **126,4° e 0,146** · B×C **156,8° e 0,568**. Nenhum par chega perto do limiar de irmãs.
>
> A peça 4 era "top-down flat lay, só mãos, tinta escura com halo". O halo foi proibido em 2026-08-04 e nada tinha substituído: a peça saiu para o feed com o chapéu a **1,43:1**. O lever "tinta escura sobre claro" continua sendo exclusivo dela, agora sustentado por contraluz de janela em vez de halo.
| 6 | Mecânicos | **196,6°** | 0,205 | 0,075 | **poça de luz âmbar de luminária + ambiente azul-petróleo, queda abrupta para a base** | over-shoulder de grupo, 85 mm | **Exo 2 Bold −3%** | branco sobre queda de luz fotográfica (sem scrim, sem sombra) | **documental mestre-aprendiz**: 3 pessoas, celular filmando o gesto |

## Copies usadas, por tipo da Mandala

| Peça | Tipo | Head |
|---|---|---|
| 1 | Revelação | Agenda lotada tem TETO |
| 2 | Reflexão | A aula acaba. O material fica. |
| 3 | Comparação | VOCÊ ENSINA 30. PODIA ENSINAR 3.000. |
| 4 | Ensino | O curso começa na aula de amanhã. |
| 5 | Oportunidade | SUA PASTA DO DRIVE VALE DINHEIRO. |
| 6 | Oportunidade | O MACETE QUE VOCÊ FAZ NO AUTOMÁTICO TEM FILA DE GENTE QUERENDO APRENDER. |

## Tentativa reprovada, para não repetir

Uma primeira versão da peça de professores usou cozinha à noite, luminária âmbar, sentada à mesa, Albert Sans, branco sobre scrim. Perfil: matiz **27,3°**, L **0,153**. Contra a peça 1 isso dava **1,3° e 0,017** de distância — irmãs no feed, mesmo com nicho, copy e objeto diferentes. **Trocar conteúdo não é trocar linguagem visual.**

## Limite conhecido da métrica

Quando a saturação é menor que ~0,05, a **matiz deixa de significar alguma coisa**. As peças 4 e 5 ficam a 14,7° de matiz uma da outra, mas com saturação 0,033 e 0,025 — ambas praticamente dessaturadas. O que as separa é ângulo (cenital × 85 mm), presença humana (só mãos × rosto), qualidade de luz (difusa × dura) e tipografia. Nesses casos julgue pela direção de arte, não pelo número.

## Alavancas ainda não usadas

- Contraluz forte com silhueta
- Cena noturna urbana, luz de neon
- Paletas: terracota, roxo (azul-petróleo gasto na peça 6)
- Direção de arte: comparação em duas metades, humor por personificação, UGC amador
- Tipografia: Manrope Light em corpo grande (Exo 2 gasto na peça 6)

## Atenção — variantes não entregues que colidem com a peça 6

A auditoria de 2026-08-04 mediu as variantes de professores `professora-auditorio` (ΔHue 1,3° + ΔL 0,039) e `professora-tela` (ΔHue 8,5° + ΔL 0,031) contra a peça 6 de mecânicos: **abaixo do limiar de irmãs**. Se qualquer uma dessas variantes entrar no mesmo conjunto Andromeda que a peça 6, uma das duas muda de paleta.

## Como conferir

```python
def perfil(png):
    a = np.asarray(Image.open(png).convert('RGB')).astype(np.float64)/255.0
    r,g,b = a[:,:,0].mean(), a[:,:,1].mean(), a[:,:,2].mean()
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    L = 0.2126*lin(a[:,:,0])+0.7152*lin(a[:,:,1])+0.0722*lin(a[:,:,2])
    return h*360, s, L.mean(), L.std()
```

Matiz a menos de 20° **somada** a luminância a menos de 0,05 reprova. E confira quantas das seis alavancas mudaram: menos de quatro é achado.
