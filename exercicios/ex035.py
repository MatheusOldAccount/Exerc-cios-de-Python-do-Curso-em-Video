reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta3 > reta2:
    t = reta3 - reta2
else:
    t = reta2 - reta1
if reta2+reta3 > reta1 > t:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')
