lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #lista[-1] = lista[len(lista)-1]
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        d = 0
        while d < len(lista):
            if n <= lista[d]:
                lista.insert(d, n)
                print(f'Adicionado na posição {d} da lista...')
                break
            d += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
