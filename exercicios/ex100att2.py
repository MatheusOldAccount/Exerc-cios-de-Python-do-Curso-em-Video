from random import randint
from time import sleep


def sorteia(lst):
    x = 1
    print('Sorteando 5 valores da lista: ', end='')
    while x <= 5:
        n = randint(1, 10)
        if n not in lst:
            lst.append(n)
            print(f'{n} ', end='')
            x += 1
            sleep(0.3)
    print('PRONTO!')


def somaPar(l):
    soma = 0
    for elemento in l:
        if elemento % 2 == 0:
            soma += elemento
    print(f'Somando os valores pares de {l}, temos {soma}')


lista = list()
sorteia(lista)
somaPar(lista)
