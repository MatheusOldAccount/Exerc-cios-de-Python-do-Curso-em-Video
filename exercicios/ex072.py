tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
indice = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= indice <= 20:
        break
    indice = int(input(('Tente novamente. Digite um número entre 0 e 20: ')))
print(f'Você digitou o número {tupla[indice]}')
