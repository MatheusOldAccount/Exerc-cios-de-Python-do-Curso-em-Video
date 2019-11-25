lista = list()
data = []
for line in range(0, 3):
    for column in range(0, 3):
        data.append(int(input(f'Digite um valor para [{line}, {column}]: ')))
    lista.append(data[:])
    data.clear()
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}] ', end='')
    print()
