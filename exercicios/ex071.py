print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
val = int(input('Que valor você quer sacar? R$'))
tot50 = tot20 = tot10 = tot1 = 0
while True:
    while val >= 50:
        val -= 50
        tot50 += 1
    while val >= 20:
        val -= 20
        tot20 += 1
    while val >= 10:
        val -= 10
        tot10 += 1
    while val > 0:
        val -= 1
        tot1 += 1
    if val == 0:
        break
if tot50 > 0:
    print(f'Total de {tot50} cédula(s) de R$50')
if tot20 > 0:
    print(f'Total de {tot20} cédula(s) de R$20')
if tot10 > 0:
    print(f'Total de {tot10} cédula(s) de R$10')
if tot1 > 0:
    print(f'Total de {tot1} cédula(s) de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
