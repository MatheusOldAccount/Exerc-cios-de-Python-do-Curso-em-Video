print('-'*20)
print('{:^20}'.format('LOJA SUPER BARATÃO'))
print('-'*20)
tot = amount = qtde = 0
while True:
    product = str(input('Nome do Produto: ')).strip().replace(' ', '').capitalize()
    price = float(input('Preço : R$'))
    if price > 1000:
        amount += 1
    tot += price
    if qtde == 0 or price < valuecheap:
        cheap = product
        valuecheap = price
    continues = ' '
    while continues not in 'SN':
        continues = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continues == 'N':
        break
    qtde += 1
print('{:-^25}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {amount} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {cheap} que custa R${valuecheap:.2f}')
