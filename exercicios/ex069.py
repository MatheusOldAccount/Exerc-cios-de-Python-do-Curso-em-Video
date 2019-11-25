txt = 'CADASTRE UMA PESSOA'
totmaior = homem = mulher = 0
print('-'*30)
while True:
    sexo = escolha = ''
    print(f'{txt:^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 30)
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 30)
    if idade > 18:
        totmaior += 1
    if sexo == 'M':
        homem += 1
    else:
        if idade < 20:
            mulher += 1
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totmaior}')
print(f'Ao todo temos {homem} homem(ns) cadastrado(s)')
print(f'E temos {mulher} mulher(es) com menos de 20 anos')
