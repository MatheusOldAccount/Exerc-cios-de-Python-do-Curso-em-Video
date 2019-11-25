tot = qtd = repeat = valcheap = 0
cheap = ''
while True:
    name = str(input('Digite o nome do produto: ')).strip()
    price = float(input('Digite o preço do produto: R$'))
    tot += price
    if price >= 1000:
        qtd += 1
    if repeat == 0:
        cheap = name
        valcheap = price
    else:
        if price < valcheap:
            cheap = name
            valcheap = price
    repeat += 1
    option = 'a'
    while option not in 'sSNn':
        option = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if option == 'N':
        break
print(f'Total gasto: R${tot:.2f}')
print(f'{qtd} produto(s) custa(m) mais de R$1000,00')
print(f'O nome do produto mais barato é {cheap} com preço de R${valcheap:.2f}')
