p1 = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A : '))
décimo = razão * 10 + p1
while p1 < décimo:
    print('{} -> '.format(p1), end='')
    p1 += razão
print('Acabou')
qtde = int(input('Deseja ver mais termos da P.A? Se sim digite quantos termos, senão, digite 0: '))
while qtde != 0:
    print('{} -> '.format(p1), end='')
    p1 += razão
    qtde -= 1
    if qtde == 0:
        print('Acabou')
        qtde = int(input('Deseja ver mais termos da P.A? Se sim digite quantos termos, senão, digite 0: '))
    elif qtde < 0:
        print('Não é possível ver termos negativos. Considerando como querendo ver 1 termo: ')
        qtde = 1
print('Programa Encerrado')
