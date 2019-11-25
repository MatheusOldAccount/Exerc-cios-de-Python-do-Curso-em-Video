distancia = int(input('Distância da viagem em KM: '))
print('O preço da passagem é de R${:.2f}'.format(distancia * 0.5) if distancia <= 200 else ('O preço da passagem é de R${:.2f}'.format(distancia*0.45)))

