from datetime import date
nasc = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: MASTER')
