totalpessoas = list()
pessoaindividual = dict()
tot = totidade = 0
while True:
    pessoaindividual['nome'] = str(input('Nome: ')).strip().capitalize()
    sex = str(input('Sexo: [M/F] ')).strip()[0]
    while sex not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        sex = str(input('Sexo: [M/F] ')).strip()[0]
    pessoaindividual['sexo'] = sex
    age = int(input('Idade: '))
    pessoaindividual['idade'] = age
    totalpessoas.append(pessoaindividual.copy())
    tot += 1
    totidade += age
    continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
    while continuar not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'A) Ao todo temos {tot} pessoas cadastradas.')
media = totidade / tot
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for dic in totalpessoas:
    if dic['sexo'] in 'Ff':
        print(f'{dic["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for avg in totalpessoas:
    if avg['idade'] > media:
        print(f'nome = {avg["nome"]}; sexo = {avg["sexo"].upper()}; idade = {avg["idade"]};')
print('<< ENCERRADO >> ')
