tot = []
jogador = dict()
gol = list()
while True:
    print('-' * 30)
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    departures = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    cont = soma = 0
    while cont < departures:
        golfeito = int(input(f'Quantos gols na partida {cont}? '))
        gol.append(golfeito)
        soma += golfeito
        cont += 1
    jogador['tot'] = soma
    jogador['gols'] = gol[:]
    gol.clear()
    proceed = str(input('Quer continuar? [S/N] ')).strip()[0]
    tot.append(jogador.copy())
    if proceed in 'Nn':
        break
print('-=' * 30)
print(f'{"cod":>5} {"nome":<20}{"total":<15}{"gols"}')
print('-' * 40)
for c, v in enumerate(tot):
    print(f'{c:>5} {v["nome"]:<20}{v["tot"]:<15}{v["gols"]}')
print('-' * 40)
while True:
    option = int(input('Mostrar dados de qual jogador? '))
    if option < 0 or option >= len(tot) and option != 999:
        print(f'ERRO! Não existe jogador com código {option}! Tente novamente.')
    elif option == 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {tot[option]["nome"]}:')
        for jogo, qtdgols in enumerate(tot[option]['gols']):
            print(f'No jogo {jogo} fez {qtdgols} gols.')
print('<<< VOLTE SEMPRE >>>')
