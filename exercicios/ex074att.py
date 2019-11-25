from random import randint
v0 = randint(1, 10)
v1 = randint(1, 10)
v2 = randint(1, 10)
v3 = randint(1, 10)
v4 = randint(1, 10)
tupla = (v0, v1, v2, v3, v4)
print(f'Os valores sorteados foram: ', end='')
for value in tupla:
    print(f'{value}', end=' ')
for cont, value in enumerate(tupla):
    if cont == 0:
        maior = value
        menor = value
    else:
        if value > maior:
            maior = value
        if value < menor:
            menor = value
print(f'\nO maior valor sorteado foi {maior}\nO menor valor sorteado foi {menor}')
