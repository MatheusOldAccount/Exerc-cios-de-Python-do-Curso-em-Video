fat = int(input('Você deseja ver o fatorial de qual número? '))
resultado = 1
for c in range(fat, 0, -1):
    resultado *= c
print('O fatorial de {} é: {}'.format(fat, resultado))
