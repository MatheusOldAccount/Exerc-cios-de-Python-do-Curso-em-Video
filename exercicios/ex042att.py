seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 > seg2:
    diferença = seg1 - seg2
else:
    diferença = seg2 - seg1
if diferença < seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if seg1 == seg2 and seg1 == seg3:
    #podemos por if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
    #podemos por elif seg1 != seg2 != seg3 != seg1
    #q significa o seg1 é diferente do seg2 q é diferente do seg3 que é diferente do seg1
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')


