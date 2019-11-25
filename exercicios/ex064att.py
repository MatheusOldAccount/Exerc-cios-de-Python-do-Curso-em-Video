num = 0
qtde = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        qtde += 1
        soma += num
if qtde == 0:
    print('Você não digitou nenhum número')
elif qtde == 1:
    print('Você digitou 1 único número que é {}'.format(soma))
else:
    print('Você digitou {} números e a soma entre eles foi {}.'.format(qtde, soma))
