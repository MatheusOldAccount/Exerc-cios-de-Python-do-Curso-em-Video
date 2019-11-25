variable = list()
for c in range(1, 6):
    variable.append(int(input(f'Digite o {c}º valor: ')))
for pos, value in enumerate(variable):
    if pos == 0:
        smaller = bigger = value
    else:
        if value > bigger:
            bigger = value
        if value < smaller:
            smaller = value
print('-='*30)
print(f'Você digitou os valores {variable}')
print(f'O maior valor digitado foi {bigger} na(s) posição(ões) ', end='')
for pos, value in enumerate(variable):
    if value == bigger:
        print(f'{pos}...', end=' ')
print()
print(f'O menor valor digitado foi {smaller} na(s) posição(ões) ', end='')
for pos, value in enumerate(variable):
    if value == smaller:
        print(f'{pos}...', end=' ')
