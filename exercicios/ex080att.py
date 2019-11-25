valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista... ')
    else:
        d = 0
        while d < len(valores):
            if n <= valores[d]:
                valores.insert(d, n)
                print(f'Adicionado na posição {d} da lista... ')
                break
            d += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
