from time import sleep
from random import randint
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
listagame = []
listatemp = list()
draw = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {draw} JOGOS -=-=-=')
while True:
    for c in range(1, 7):
        n = randint(1, 60)
        while n in listatemp:
            n = randint(1, 60)
        listatemp.append(n)
    listatemp.sort()
    listagame.append(listatemp[:])
    listatemp.clear()
    draw -= 1
    if draw == 0:
        break
for l in listagame:
    draw += 1
    print(f'Jogo {draw}: {l}')
    sleep(1)
print(f'{"-=" * 5} < BOA SORTE ! > {"-=" * 5}')
