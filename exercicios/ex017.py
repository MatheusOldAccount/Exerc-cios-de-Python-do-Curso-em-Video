from math import sqrt
catetooposto = float(input('Digite o comprimento do cateto oposto: '))
catetoadjacente = float(input('Digite o comprimento do cateto adjacente '))
hip = (catetooposto**2) + (catetoadjacente**2)
print('Comprimento da hipotenusa: {:.2f}'.format(sqrt(hip)))
