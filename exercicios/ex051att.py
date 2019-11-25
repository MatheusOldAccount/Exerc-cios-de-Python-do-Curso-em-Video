print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)
p1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = p1 + (10 - 1) * razão
for c in range(p1, décimo + razão, razão):
    print('{} -> '.format(c), end='')
print('ACABOU')
