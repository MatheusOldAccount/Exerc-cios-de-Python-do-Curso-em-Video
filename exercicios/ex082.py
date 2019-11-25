lista1 = list()
while True:
    lista1.append(int(input('Digite um número: ')))
    proceed = str(input('Quer continuar? ')).strip().upper()[0]
    if proceed == 'N':
        break
print('-='*30)
print(f'A lista completa é {lista1}')
listapar = []
listaimpar = []
for c, v in enumerate(lista1):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
