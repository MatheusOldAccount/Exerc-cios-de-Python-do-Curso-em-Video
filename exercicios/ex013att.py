sal = float(input('Qual é o salário do Funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, ((sal*15/100) + sal)))
