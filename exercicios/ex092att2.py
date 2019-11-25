from datetime import date
dicionário = dict()
dicionário['name'] = str(input('Nome: ')).strip().capitalize()
birthday = int(input('Ano de Nascimento: '))
dicionário['age'] = date.today().year - birthday
dicionário['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionário['ctps'] != 0:
    dicionário['contratação'] = int(input('Ano de Contratação: '))
    dicionário['salário'] = float(input('Salário: R$'))
    dicionário['aposentadoria'] = dicionário['contratação'] - birthday + 35
print('-=' * 30)
print(dicionário)
for k, v in dicionário.items():
    print(f'  -- {k} tem o valor {v}')
