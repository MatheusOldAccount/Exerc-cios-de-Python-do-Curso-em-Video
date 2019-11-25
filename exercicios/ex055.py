for i in range(0, 5):
    peso = float(input('Digite seu peso em KG: '))
    if i == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso digitado foi: {:.2f}KG '.format(maior))
print('O menor peso digitado foi: {:.2f}KG '.format(menor))
