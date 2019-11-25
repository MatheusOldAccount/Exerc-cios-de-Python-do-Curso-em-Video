def leiaInt(texto):
    while True:
        num = str(input(texto))
        if num.isnumeric():
            num = int(num)
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num


# Programa Principal
print('-' * 30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
