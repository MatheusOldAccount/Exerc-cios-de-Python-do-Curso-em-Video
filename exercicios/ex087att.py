lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumcolumn = par = 0
for line in range(0, 3):
    for column in range(0, 3):
        lista[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}] ', end='')
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
        if c == 2:
            sumcolumn += lista[l][2]
        if l == 1:
            if c == 0:
                maior = lista[1][0]
            else:
                if lista[1][c] > maior:
                    maior = lista[1][c]
    print()
print('-=' * 40)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {sumcolumn}.')
print(f'O maior valor da segunda linha é {maior}.')
