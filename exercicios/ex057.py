sexo = ''
val = 0
while sexo != 'M' and sexo != 'F':
    val += 1
    if val == 0:
        print('Digite seu Sexo: ')
        sexo = str(input('Digite seu sexo [M/F] : ')).upper()
    else:
        sexo = str(input('Digite seu sexo [M/F] : ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo Inválido ! Digite novamente')
print('Sexo : {}'.format(sexo))
