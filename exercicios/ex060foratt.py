n = int(input('Digite um número para calcular seu Fatorial: '))
resultado = 1
print('Calculando {}! = '.format(n), end='')
for cont in range(n, 0, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    resultado *= cont
print('{}'.format(resultado), end='')
