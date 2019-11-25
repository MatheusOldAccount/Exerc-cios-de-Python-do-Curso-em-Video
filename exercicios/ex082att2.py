lista = list()
evenlist = []
oddlist = []
while True:
    lista.append(int(input('Digite um número: ')))
    proceed = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if proceed == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
for value in lista:
    if value % 2 == 0:
        evenlist.append(value)
    else:
        oddlist.append(value)
print(f'A lista de pares é {evenlist}')
print(f'A lista de ímpares é {oddlist}')
