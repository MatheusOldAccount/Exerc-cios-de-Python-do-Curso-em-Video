print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 10
qtde = 0
while cont >= 1:
    print('{} -> '.format(p1), end='')
    p1 += razão
    qtde += 1
    cont -= 1
    if cont == 0:
        print('PAUSA')
        cont = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termo(s) mostrado(s).'.format(qtde))
