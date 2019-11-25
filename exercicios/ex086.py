lista = list()
data = []
for line in range(0, 3):
    for column in range(0, 3):
        data.append(int(input(f'Digite um valor para: [{line}, {column}]: ')))
    lista.append(data[:])
    data.clear()
print('-=' * 30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{lista[c][d]:^5}]', end=' ')
    print()
