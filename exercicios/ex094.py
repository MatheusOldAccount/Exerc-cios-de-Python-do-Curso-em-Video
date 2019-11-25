totdados = []
dadospessoa = {}
somaidade = media = 0
while True:
    dadospessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    dadospessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    age = int(input('Idade: '))
    somaidade += age
    dadospessoa['idade'] = age
    totdados.append(dadospessoa.copy())
    proceed = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if proceed == 'N':
        break
media = somaidade / len(totdados)
print('-=' * 30)
print(f'- O grupo tem {len(totdados)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for dados in totdados:
    if dados['sexo'] == 'F':
        print(dados['nome'], end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for d in totdados:
    if d['idade'] > media:
        print(f'\nnome = {d["nome"]}; sexo = {d["sexo"]}; idade = {d["idade"]};')
print('<<< ENCERRADO >>>')
