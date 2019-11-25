def leiaInt(txt):
    global c
    while True:
        válido = False
        try:
            n1 = int(input(txt))
        except KeyboardInterrupt:
            print(f'\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return ''
            c += 1
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            válido = True
            return f'O valor inteiro digitado foi {n1} '
        if válido:
            break


def leiaReal(txt):
    global c
    while True:
        if c == 1:
            return ''
        valid = False
        try:
            n2 = float(input(txt))
        except KeyboardInterrupt:
            print(f'\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return ''
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        else:
            valid = True
            return f'e o real foi {n2}'
        if valid:
            break


c = 0
r1 = leiaInt('Digite um Inteiro: ')
r2 = leiaReal('Digite um Real: ')
print(f'{r1}{r2}')
