from random import randint
n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
tupla = (n1, n2, n3, n4, n5)
print('Os valores sorteados foram:', end=' ')
for c in tupla:
    print(f'{c}', end=' ')
    if c == n1:
        maior = n1
        menor = n1
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print('')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
