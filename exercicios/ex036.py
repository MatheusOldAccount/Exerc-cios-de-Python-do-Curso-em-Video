valor = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos você irá pagar? '))
prest = (valor / anos) / 12
if prest > sal*(30/100):
    print('O empréstimo foi negado, pois a prestação mensal de R${:.2f} é maior que 30% do seu salário que corresponde a R${:.2f}'.format(prest, sal*(30/100)))
else:
    print('Empréstimo efetuado. Será pago {} meses de R${:.2f} cada um'.format(anos * 12, prest))

