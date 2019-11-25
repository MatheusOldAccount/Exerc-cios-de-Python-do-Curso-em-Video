distancia = int(input('Distância da viagem em KM: '))
if distancia <= 200:
    print('O preço da passagem é de R${:.2f}'.format(distancia * 0.5))
else:
    print('O preço da passagem é de R${:.2f}'.format(distancia*0.45))
