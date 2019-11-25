print('-' * 40)
print('{:^40}'.format('Sequência de Fibonacci'))
print('-' * 40)
fibo = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
cont = fibo
while cont > 0:
    if cont == fibo:
        print('{} -> '.format(a), end='')
    elif cont == fibo - 1:
        print('{} -> '.format(b), end='')
    else:
        c = a + b
        a = b
        b = c
        print('{} -> '.format(c), end='')
    cont -= 1
print('FIM')
