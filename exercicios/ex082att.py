lista = list()
evenlist = []
oddlist = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        evenlist.append(n)
    else:
        oddlist.append(n)
    lista.append(n)
    proceed = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if proceed == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {evenlist}')
print(f'A lista de ímpares é {oddlist}')
