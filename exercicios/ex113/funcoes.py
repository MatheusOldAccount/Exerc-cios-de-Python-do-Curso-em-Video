def leiaInt(txt):
    while True:
        válido = False
        try:
            n1 = int(input(txt))
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            válido = True
            return f'O valor inteiro digitado foi {n1} '
        if válido:
            break


def leiaReal(txt):
    while True:
        valid = False
        try:
            n2 = float(input(txt))
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        else:
            valid = True
            return f'e o real foi {n2}'
        if valid:
            break
