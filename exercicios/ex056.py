totalidade = 0
nomemaisvelho = ''
quantidade = 0
maisvelho = 0
for a in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).upper()
    totalidade += idade
    if idade > maisvelho and sexo == 'MASCULINO' or sexo == 'M':
        maisvelho = idade
        nomemaisvelho = str(nome)
    if sexo == 'FEMININO' or sexo == 'F' and idade < 20:
        quantidade += 1
mediaidade = totalidade / 4
print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print('{} mulher(es) têm menos de 20 anos.'.format(quantidade))
if maisvelho == 0:
    print('Nenhuma pessoa do sexo Masculino foi digitada')
else:
    print('O nome do homem mais velho do grupo é {}'.format(nomemaisvelho))
