fat = int(input('Você deseja ver o fatorial de qual número? '))
resultado = 1
while fat > 0:
    resultado *= fat
    fat -= 1
print('Seu fatorial é: {}'.format(resultado))
