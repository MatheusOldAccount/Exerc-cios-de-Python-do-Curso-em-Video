soma = 0
for i in range(1, 7):
    val = int(input('Digite um valor: '))
    if val % 2 == 0:
        soma += val
print('A soma dos pares é : {}'.format(soma))
