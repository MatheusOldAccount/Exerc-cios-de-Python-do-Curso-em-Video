people = list()
data = []
qtd = 0
while True:
    name = str(input('Nome: ')).strip()
    weight = float(input('Peso: '))
    if qtd == 0:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        if weight < menor:
            menor = weight
    data.append(name)
    data.append(weight)
    qtd += 1
    people.append(data[:])
    data.clear()
    proceed = str(input('Quer continuar? [S/N] ')).strip()[0]
    if proceed in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {qtd} pessoa(s).')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for w in people:
    if w[1] == maior:
        print(f'[{w[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for w in people:
    if w[1] == menor:
        print(f'[{w[0]}]', end=' ')
