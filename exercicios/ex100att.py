from random import choice
from time import sleep


def sorteie(lst):
    lista = []
    cont = 1
    print('Sorteando 5 valores da lista: ', end='')
    while cont < 6:
        n = choice(lst)
        if n not in lista:
            print(f'{n} ', end='')
            lista.append(n)
            cont += 1
            sleep(0.3)
    print('PRONTO!')
    lst.clear()
    lst.append(lista[:])


def soma(l):
    soma = 0
    for number in l:
        if number % 2 == 0:
            soma += number
    print(f'Somando os valores pares de {l}, temos {soma}')


números = list(range(1, 11))
sorteie(números)
soma(números[0])
