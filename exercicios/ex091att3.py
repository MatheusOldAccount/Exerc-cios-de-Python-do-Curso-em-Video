from random import randint
from operator import itemgetter
from time import sleep
jogador = dict()
print('Valores sorteados: ')
for c in range(1, 5):
    jogador[f'player{c}'] = randint(1, 6)
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
rank = list()
rank = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('   == RANKING DOS JOGADORES ==   ')
for c, va in enumerate(rank):
    print(f'    {c + 1}° lugar: {va[0]} com {va[1]}.')
    sleep(1)
