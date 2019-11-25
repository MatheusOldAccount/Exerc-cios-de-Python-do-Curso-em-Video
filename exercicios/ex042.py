l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))
if l1 > l2:
    sub = l1 - l2
else:
    sub = l2 - l1
if l1 + l2 > l3 > sub:
    print('É um triângulo', end=' ')
    if l1 == l2 and l1 == l3:
        print('Equilátero')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não é um triângulo')
