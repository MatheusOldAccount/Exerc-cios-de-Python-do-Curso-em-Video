from math import hypot, sqrt
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjascente: '))
hi = sqrt((catop ** 2) + (catad ** 2))
print('A hipotenusa vai medir {:.2f}.'.format(hi))
