def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return fat


# Programa Principal
print('-' * 30)
#print(fatorial(5, True))
print(fatorial(5, show=True))
help(fatorial)
