dicionario = dict()
acurracy = list()
dicionario['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
cont = soma = 0
while cont < partidas:
    gols = int(input(f'Quantos gols na partida {cont}? '))
    soma += gols
    acurracy.append(gols)
    cont += 1
dicionario['gols'] = acurracy[:]
dicionario['total'] = soma
print('-=' * 30)
print(dicionario)
print('-=' * 30)
for key, value in dicionario.items():
    print(f'O campo {key} tem o valor {value}.')
print('-=' * 30)
print(f'O jogador {dicionario["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {dicionario["gols"][c]} gols.')
print(f'Foi um total de {soma} gols.')
