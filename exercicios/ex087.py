lista = []
data = list()
somacoluna = somapar = 0
for line in range(0, 3):
    for column in range(0, 3):
        data.append(int(input(f'Digite um valor para [{line}, {column}]: ')))
    lista.append(data[:])
    data.clear()
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end=' ')
        if lista[l][c] % 2 == 0:
            somapar += lista[l][c]
        if c == 2:
            somacoluna += lista[l][2]
        if l == 1 and c == 0:
            maior = lista[1][c]
        elif l == 1:
            if lista[1][c] > maior:
                maior = lista[1][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somacoluna}.')
print(f'O maior valor da segunda linha é {maior}.')
