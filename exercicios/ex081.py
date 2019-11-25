lista = list()
qtd = 0
while True:
    lista.append(int(input('Digite um número: ')))
    qtd += 1
    proceed = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if proceed == 'N':
        break
print(f'Você digitou {qtd} elemento(s)')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista! E está na posição {lista.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista!')
