lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    proceed = str(input('Quer continuar? [S/N] ')).strip()[0]
    if proceed in 'nN':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elemento(s).')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista: #lista.count(5) > 0:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado dentro da lista!')
