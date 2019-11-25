from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
#hj = date.today().year
#idade = hj - ano
#ou :
hj = date.today()
idade = hj.year - ano
if idade < 18:
    print('Ainda vai se alistar. Faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print('Já passou do tempo de alistamento. Já passarou(am) {} ano(s) que você devia ter se alistado.'.format(idade - 18))
