print('='*25)
print('{:^25}'.format('BANCO CEV'))
print('='*25)
val = int(input('Que valor você quer sacar? R$'))
tot50 = tot20 = tot10 = tot1 = 0
while True:
    while val >= 50:
        tot50 += 1
        val -= 50
    while val >= 20:
        tot20 += 1
        val -= 20
    while val >= 10:
        tot10 += 1
        val -= 10
    while val > 0:
        tot1 += 1
        val -= 1
    if val == 0:
        break
if tot50 > 0:
    print(f'Total de {tot50} cédulas de R$50')
if tot20 > 0:
    print(f'Total de {tot20} cédulas de R$20')
if tot10 > 0:
    print(f'Total de {tot10} cédulas de R$10')
if tot1 > 0:
    print(f'Total de {tot1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
