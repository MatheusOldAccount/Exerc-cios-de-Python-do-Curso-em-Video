def area(larg, compr):
    ar = larg * compr
    print(f'A área de um terreno {larg:.1f}x{compr:.1f} é de {ar:.1f}m²')


print('Controle de Terrenos')
print('-' * 25)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
  