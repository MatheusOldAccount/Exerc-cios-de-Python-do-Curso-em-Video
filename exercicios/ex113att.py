def leiaReal(texto):
    valido = False
    while True:
        try:
            nfloat = float(input(texto))
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        else:
            valido = True
        if valido:
            break
    return f'e o real foi {nfloat}'


def leiaInt(txt):
    valid = False
    while True:
        try:
            nint = int(input(txt))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            valid = True
        if valid:
            break
    print(f'O valor inteiro digitado foi {nint} {leiaReal("Digite um Real: ")}')


leiaInt('Digite um Inteiro: ')
