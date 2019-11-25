p1 = int(input('Digite o primeiro termo da P.A : '))
razão = int(input('Digite a razão da P.A : '))
décimo = p1 + (10 - 1) * razão
while p1 <= décimo:
    print('{} -> '.format(p1), end='')
    p1 += razão
print('Acabou')
