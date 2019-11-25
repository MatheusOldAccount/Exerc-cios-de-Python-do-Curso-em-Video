dicionario = dict()
dicionario['Name'] = str(input('Nome: ')).strip().capitalize()
dicionario['Average'] = float(input(f'Média de {dicionario["Name"]}: '))
if dicionario['Average'] >= 7:
    dicionario['Situation'] = 'Aprovado'
else:
    dicionario['Situation'] = 'Reprovado'
for k, v in dicionario.items():
    print(f'{k} é igual a {v}')
