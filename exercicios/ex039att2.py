from datetime import date
ano = int(input('Ano de nascimento: '))
sexo = str(input('Sexo -> [M/F]: ')).upper()
anotual = date.today().year
idade = anotual - ano
if sexo == 'F':
    print('Por ser mulher não é necessário o alistamento.')
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, anotual))
    if idade < 18:
        print('Ainda faltam {} ano(s) para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(ano + 18))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} ano(s).'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(ano + 18))
    else:
        print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, anotual))
        print('Você tem que se alistar IMEDIATAMENTE!')
