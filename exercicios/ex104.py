def leiaInt(txt):
    var = str(input(txt))
    while not var.isnumeric():
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        var = str(input(txt))
    return var


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {int(n)}')
