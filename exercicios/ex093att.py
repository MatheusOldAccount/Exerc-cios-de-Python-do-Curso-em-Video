jogador = {'nome': str(input('Nome do Jogador: ')).strip().capitalize()}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
totgols = 0
for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c}? '))
    gols.append(gol)
    totgols += gol
jogador['gols'] = gols[:]
jogador['total'] = totgols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c, va in enumerate(jogador['gols']):
    print(f'    => Na partida {c}, fez {va} gols.')
print(f'Foi um total de {jogador["total"]}')
