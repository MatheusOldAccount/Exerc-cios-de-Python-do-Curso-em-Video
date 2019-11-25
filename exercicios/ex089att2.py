lista = list()
dados = []
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    proceed = str(input('Quer continuar? [S/N]')).strip()[0]
    if proceed in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":>5} {"NOME":<15} {"Média":<2}')
print('-' * 25)
for posicao, cadastro in enumerate(lista):
    print(f'{posicao:>5} {cadastro[0]:<15} {(cadastro[1] + cadastro[2]) / 2:<5.1f}')
print('-' * 30)
while True:
    option = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if option == 999:
        break
    elif option >= len(lista) or option < 0:
        print('Opção inválida!')
    else:
        print(f'Notas de {lista[option][0]} são [{lista[option][1]}, {lista[option][2]}]')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
