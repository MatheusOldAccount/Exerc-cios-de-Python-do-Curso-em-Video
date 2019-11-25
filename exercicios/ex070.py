print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
price = tot = qtde = 0
while True:
    checks = ''
    product = str(input('Nome do Produto: ')).capitalize()
    value = float(input('Preço: R$'))
    if qtde == 0:
        cheap = value
        namecheap = product
    elif value < cheap:
        cheap = value
        namecheap = product
    while checks != 'N' and checks != 'S':
        checks = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    price += value
    if value > 1000:
        tot += 1
    qtde += 1
    if checks == 'N':
        print('{:-^30}'.format('FIM DO PROGRAMA'))
        break
print(f'O total da compra foi R${price:.2f}')
print(f'Temos {tot} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {namecheap} que custa R${cheap:.2f}')
