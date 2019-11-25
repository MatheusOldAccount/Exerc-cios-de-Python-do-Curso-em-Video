from random import randint
from time import sleep
dicionario = {}
print('Valores sorteados: ')
cont = 0
for c in range(1, 5):
    num = randint(1, 6)
    dicionario[f'Jogador{c}'] = randint(1, 6)
    print(f'O Jogador{c} tirou {num}')
'''    if c == 0 or num > mai:
        mai = num
        pos = f'Jogador{c}'
print(f'Vencedor: {pos} com {mai}')
'''
for c in sorted(dicionario.values(), reverse=True):
    cont += 1
    print(f'{cont}° lugar: {c}')
