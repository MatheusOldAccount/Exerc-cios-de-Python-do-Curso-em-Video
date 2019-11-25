from time import sleep


def ajuda(function):
    print(f'\033[m\033[1;30;44m~' * 50)
    print(f'{f"Acessando o manual do comando {function}":^50}')
    print(f'~' * 50)
    sleep(2)
    print('\033[m\033[7;30m')
    help(function)


while True:
    print(f'\033[m\033[1;30;42m~' * 30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print(f'~' * 30)
    opc = str(input('\033[mFunção ou Biblioteca > '))
    if opc.upper() == 'FIM':
        break
    ajuda(opc)
print(f'\033[m\033[1;30;41m~' * 15)
print(f'{"ATÉ LOGO":^15}')
print(f'~' * 15)
