sal = float(input('Digite o seu salário: R$'))
if sal > 1250:
    sal = sal + sal*(10/100)
else:
    sal = sal + sal*(15/100)
print('Seu salário é de R${:.2f}'.format(sal))
