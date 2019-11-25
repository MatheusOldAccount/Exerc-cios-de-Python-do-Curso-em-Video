from random import randint
from time import sleep
lista = []
data = []
cont = 0
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"-=" * 3}  SORTEANDO {n} JOGOS  {"-=" * 3}')
for c in range(1, n + 1):
    for d in range(1, 7):
        pc = randint(1, 60)
        while pc in data:
            pc = randint(1, 60)
        data.append(pc)
    data.sort()
    lista.append(data[:])
    data.clear()
for el in lista:
    cont += 1
    print(f'Jogo {cont}: {el}')
    sleep(1)
print(f'{"-=" * 5} < BOA SORTE! > {"-=" * 5}')
