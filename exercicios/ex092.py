from datetime import date
dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dicionario['idade'] = date.today().year - nasc
dicionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: R$ '))
    dicionario['aposentadoria'] = dicionario['contratação'] - nasc + 35
print('-=' * 30)
print(dicionario)
for k, v in dicionario.items():
    print(f'{k} tem o valor {v}')
