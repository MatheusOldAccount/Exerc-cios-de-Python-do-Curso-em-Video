a = 1
ini = int(input('Digite o primeiro termo da P.A: '))
passo = int(input('Digite a razão dessa P.A: '))
for c in range(ini, ini+passo*10, passo):
    print('{}° termo = {}'.format(a, c))
    a += 1
