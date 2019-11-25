val = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(val, anos, val / (anos * 12)))
if val / (anos * 12) > sal * 30/100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo PODE SER CONCEDIDO !')
