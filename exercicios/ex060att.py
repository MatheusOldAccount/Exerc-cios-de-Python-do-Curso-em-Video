fat = int(input('Digite um número para\ncalcular seu Fatorial: '))
print('Calculando {}! ='.format(fat), end=' ')
resultado = 1
while fat > 0:
    if fat == 1:
        print('{} ='.format(fat), end=' ')
    else:
        print('{} x'.format(fat), end=' ')
    resultado *= fat
    fat -= 1
print('{}'.format(resultado))
