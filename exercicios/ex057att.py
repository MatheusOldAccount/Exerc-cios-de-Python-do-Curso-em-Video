sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()
print('Sexo {} tegistrado com sucesso.'.format(sexo))
