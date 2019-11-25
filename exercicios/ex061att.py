print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 0
while cont < 10:
    print('{} -> '.format(p1), end='')
    p1 += razão
    cont += 1
print('FIM')
