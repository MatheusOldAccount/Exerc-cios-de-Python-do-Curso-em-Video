cont = 0
soma = 0
verificador = 0
while verificador != 999:
    verificador = int(input('Digite um número: '))
    if verificador != 999:
        soma += verificador
        cont += 1
print('A quantidade de números digitados foi: {} e a soma de todos eles é: {}'.format(cont, soma))
