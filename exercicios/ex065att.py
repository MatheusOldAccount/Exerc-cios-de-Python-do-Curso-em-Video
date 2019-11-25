res = 'S'
soma = qtde = 0
while res != 'N':
    num = int(input('Digite um número: '))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    qtde += 1
    soma += num
    if qtde == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / qtde
print('Você digitou {} número(s) e a média foi {:.2f}'.format(qtde, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
