vel = float(input('Qual é a velocidade do carro em KM/H? '))
if vel > 80:
    print('Por ultrapassar a velocidade, você foi multado em R${:.2f}'.format((vel-80)* 7))
else:
    print('Você está andando dentro da velocidade permitida e por isso não foi multado, PARABÉNS!')
