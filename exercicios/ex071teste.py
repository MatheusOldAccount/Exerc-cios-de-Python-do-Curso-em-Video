val = int(input('Valor a ser sacado: R$'))
qtd50 = qtd20 = qtd10 = qtd1 = 0
while val >= 50:
    val -= 50
    qtd50 += 1
while val >= 20:
    val -= 20
    qtd20 += 1
while val >= 10:
    val -= 10
    qtd10 += 1
while val >= 1:
    val -= 1
    qtd1 += 1
print('Foi(ram) sacado(s): ')
if qtd50 > 0:
    print(f'{qtd50} cédula(s) de R$ 50.00')
if qtd20 > 0:
    print(f'{qtd20} cédula(s) de R$ 20.00')
if qtd10 > 0:
    print(f'{qtd10} cédula(s) de R$ 10.00')
if qtd1 > 0:
    print(f'{qtd1} cédula(s) de R$ 1.00')
