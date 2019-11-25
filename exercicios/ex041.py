from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
