def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c} x ', end='')
            if c == 1:
                print('= ', end='')
    return f


print('-' * 30)
print(fatorial(5, True))
help(fatorial)
