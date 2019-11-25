roster = list()
data = []
cont = 0
while True:
    cont += 1
    name = str(input('Nome: '))
    weight = float(input('Peso: '))
    data.append(name)
    data.append(weight)
    if cont == 1:
        bigweight = smallweight = weight
        bigname = smallname = name
    else:
        if weight > bigweight:
            bigweight = weight
            bigname = name
        if weight < smallweight:
            smallweight = weight
            smallname = name
    roster.append(data[:])
    data.clear()
    proceed = str(input('Quer continuar? [S/N] ')).strip()[0]
    if proceed in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {bigweight:.1f}Kg. Peso de ', end='')
for a in roster:
    if a[1] == bigweight:
        print(f'[{a[0]}]', end=' ')
print()
print(f'O menor peso foi de {smallweight:.1f}Kg. Peso de ', end='')
for a in roster:
    if a[1] == smallweight:
        print(f'[{a[0]}]', end=' ')
