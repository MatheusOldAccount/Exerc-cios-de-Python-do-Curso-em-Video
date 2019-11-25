from datetime import date
ano = int(input('Ano de nascimento: '))
anotual = date.today().year
idade = anotual - ano
if idade < 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, anotual))
    print('Ainda faltam {} ano(s) para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano + 18))
elif idade > 18:
    print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, anotual))
    print('Você já deveria ter se alistado há {} ano(s).'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))
else:
    print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, anotual))
    print('Você tem que se alistar IMEDIATAMENTE!')

