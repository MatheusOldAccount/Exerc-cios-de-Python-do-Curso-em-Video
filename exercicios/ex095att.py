jogadores = []
player = {}
gol = list()
while True:
    player.clear()
    player['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        gol.append(int(input(f'     Quantos gols na partida {c}? ')))
    player['gols'] = gol[:]
    gol.clear()
    player['total'] = sum(player['gols'])
    jogadores.append(player.copy())
    resp = 'a'
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod  ":>3}{"nome":<20}{"gols":<15}{"total":<5}')
print('--' * 30)
for c, v in enumerate(jogadores):
    print(f'{c:>3}  {v["nome"]:<19} {v["gols"]!s:<15s}{v["total"]:<5}')
    #Esse !s:s converte uma lista em str temporariamente, é uma função
print('--' * 30)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    elif 0 <= opc < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}: ')
        for chave, valor in enumerate(jogadores[opc]['gols']):
            print(f'    No jogo {chave} fez {valor} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {opc}! ')
    print('--' * 30)
print('<< VOLTE SEMPRE >>')
