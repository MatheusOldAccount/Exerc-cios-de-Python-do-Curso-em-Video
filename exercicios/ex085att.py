listap = list()
listai = []
lista = []
for c in range(1, 8):
    n = int(input(f'Digite o {c}°. valor: '))
    if n % 2 == 0:
        listap.append()
    else:
        listai.append()
listap.sort()
listai.sort()
lista.append(listap[:])
lista.append(listai[:])
print('-=' * 30)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')
