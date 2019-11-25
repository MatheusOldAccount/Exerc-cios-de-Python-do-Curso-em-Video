qtd = 0
núm = int(input('Digite um número: '))
for c in range(1, núm+1):
    if núm % c == 0:
        qtd += 1
        print(f'\033[33m{c}', end = ' ')
    else:
        print(f'\033[31m{c}', end=' ')
print('\033[m')
if qtd == 2:
    print('Como o número só é divisível por 1 e por ele mesmo, ele é PRIMO')
else:
    print(f'Como o número é divisível por {qtd} números, ele NÃO É PRIMO')