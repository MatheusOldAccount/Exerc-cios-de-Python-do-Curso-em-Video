def pyhelp(cmd):
    from time import sleep
    string2 = f"Acessando o manual do comando '{cmd}'"
    tam2 = int(len(string2)) + 4
    print('\033[m\033[30;44m~' * tam2)
    print(f'  {string2}')
    print('~' * tam2)
    sleep(2)
    print(f'\033[m\033[7;30m', end='')
    help(cmd)


while True:
    string = 'SISTEMA DE AJUDA PyHELP'
    tam = int(len(string)) + 4
    print('\033[m\033[30;42m~' * tam)
    print(f'  {string}')
    print('~' * tam)
    func = str(input('\033[mFunção ou Biblioteca > '))
    if func.upper() == 'FIM':
        break
    pyhelp(func)
string3 = 'ATÉ LOGO!'
tam3 = int(len(string3)) + 4
print('\033[m\033[30;41m~' * tam3)
print(f'  {string3}')
print('~' * tam3)
