def área(l, c):
    area = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {area:.1f}m².\n')


print('  Controle de Terrenos  ')
print('-' * 25)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)
