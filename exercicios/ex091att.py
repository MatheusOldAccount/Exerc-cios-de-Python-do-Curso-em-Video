from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)
             }
print('Valores Sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ordenados = list()
ordenados = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ordenados):
    print(f'    {i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
