listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*35)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('-'*35)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<25}R$', end='')
    else:
        print(f'{listagem[c]: >7.2f}')
