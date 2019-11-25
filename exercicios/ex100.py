from random import choice


def sorteie(lst):
    lista = []
    cont = 1
    while cont < 6:
        n = choice(lst)
        if n not in lista:
            lista.append(n)
            cont += 1
    lst.clear()
    lst.append(lista[:])


def soma(l):
    soma = 0
    for number in l:
        if number % 2 == 0:
            soma += number
    print(f'A soma dos pares é {soma}')


números = list(range(1, 11))
sorteie(números)
soma(números[0])
print(f'Os números sorteados foram {números[0]}')
