ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#ano bissexto é divisível por 4 e ou por 400, mas não é multiplo
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} NÃO é BISSEXTO'.format(ano))
