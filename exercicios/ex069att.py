amount18 = man = woman = 0
while True:
    gender = continues = ' '
    print('-'*20)
    print('{:^20}'.format('CADASTRE UMA PESSOA'))
    print('-' * 20)
    age = int(input('Idade: '))
    while gender not in 'MF':
        gender = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 20)
    if age > 18:
        amount18 += 1
    if gender == 'M':
        man += 1
    if gender == 'F' and age < 20:
        woman += 1
    while continues not in 'SN':
        continues = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continues == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {amount18}')
print(f'Ao todo temos {man} homem(ns) cadastrado(s)')
print(f'E temos {woman} mulher(es) com menos de 20 anos')
