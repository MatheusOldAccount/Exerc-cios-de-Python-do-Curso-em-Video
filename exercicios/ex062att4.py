print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
qtde = 10
cont = 0
tot = 0
while qtde != 0:
    tot += qtde
    while cont < tot:
        print('{} -> '.format(p1), end='')
        p1 += razão
        cont += 1
    print('Pausa')
    qtde = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termo(s) mostrado(s)'.format(tot))
