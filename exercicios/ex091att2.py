from random import randint
from time import sleep
from operator import itemgetter
game = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)
        }
print('Valores Sorteados:')
for k, v in game.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = list()
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DOS JOGADORES ==  ')
for chave, valor in enumerate(ranking):
    print(f'    {chave + 1}º posição: {valor[0]} com {valor[1]}.')
    sleep(1)
