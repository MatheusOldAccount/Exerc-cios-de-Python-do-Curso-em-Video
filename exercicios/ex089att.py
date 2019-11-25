lista = list()
data = []
data2 = []
n = 0
while True:
    data.append(n)
    n += 1
    data.append(str(input('Nome: ')).strip().capitalize())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    data2.append(n1)
    data2.append(n2)
    average = (n1 + n2) / 2
    data.append(data2[:])
    data2.clear()
    data.append(average)
    lista.append(data[:])
    data.clear()
    proceed = str(input('Quer continuar? [S/N] ')).strip()[0]
    if proceed in 'Nn':
        break
print('-=' * 50)
print(f'{"No.":<15}{"NOME":<20}{"MÉDIA"}')
print('-' * 50)
for l in range(0, n):
    for c in range(0, 3):
        if c == 0:
            print(f'{lista[l][c]:<15}', end='')
        elif c == 1:
            print(f'{lista[l][c]:<23}', end='')
        else:
            print(f'{lista[l][3]:.1f}', end='')
    print()
print('-' * 50)
while True:
    choose = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if choose == 999:
        break
    else:
        print(f'Notas de {lista[choose][1]} são [{lista[choose][2][0]:.1f}, {lista[choose][2][1]:.1f}]')
        print('-' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
