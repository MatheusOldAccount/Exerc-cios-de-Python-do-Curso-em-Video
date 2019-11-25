n = int(input('Qual número você deseja ver o fatorial? '))
fat = 1
for c in range(n, 0, -1):
    fat *= c
    print(f'{c}', end=' ')
    print('x ' if c > 1 else '= ', end='')
print(f'{fat}')
print(f'O fatorial de {n} é {fat}')
