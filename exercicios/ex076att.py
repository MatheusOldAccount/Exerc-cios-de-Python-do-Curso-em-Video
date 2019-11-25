print('-'*36)
print('{:^36}'.format('LISTAGEM DE PREÇOS'))
print('-'*36)
tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)
for pos, value in enumerate(tupla):
    if pos % 2 == 0:
        print('{:.<25}'.format(value), end='')
    else:
        print('R${:>8.2f}'.format(value))
print('-'*36)
