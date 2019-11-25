print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 0
qtde = 0
while cont < 10:
    print('{} -> '.format(p1), end='')
    p1 += razão
    cont += 1
    qtde += 1
print('PAUSA')
continuação = int(input('Quantos termos você quer mostrar a mais? '))
while continuação > 0:
    print('{} -> '.format(p1), end='')
    p1 += razão
    continuação -= 1
    qtde += 1
    if continuação == 0:
        print('PAUSA')
        continuação = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termo(s) mostrado(s).'.format(qtde))
