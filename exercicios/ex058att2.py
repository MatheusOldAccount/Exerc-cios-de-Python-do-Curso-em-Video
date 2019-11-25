from random import randint
print('Sou seu computador... ')
pc = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
escolha = 15
tentativa = 0
while pc != escolha:
    escolha = int(input('Qual é seu palpite? '))
    tentativa += 1
    if pc > escolha:
        print('Mais... Tente mais uma vez.')
    elif pc < escolha:
        print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativa(s). Parabéns!'.format(tentativa))
