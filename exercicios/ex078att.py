lista = []
for c in range(0, 5):
    num = int(input(f'Digite um valor para a Posição {c}: '))
    lista.append(num)
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}', end='... ')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for d, va in enumerate(lista):
    if va == menor:
        print(f'{d}', end='... ')
