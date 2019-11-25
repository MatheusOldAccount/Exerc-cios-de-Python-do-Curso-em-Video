soma = 0
cont = 0
for tot in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(tot)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma do(s) {} número(s) pares digitados é {}'.format(cont, soma))
