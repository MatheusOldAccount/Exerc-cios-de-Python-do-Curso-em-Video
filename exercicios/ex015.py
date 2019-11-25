km = float(input('Quantidade de KM percorridos: '))
dias = int(input('Quantidade de dias que ele foi alugado: '))
preco = (60*dias) + (0.15 * km)
print('Preço a pagar: R$ {:.2f}'.format(preco))
