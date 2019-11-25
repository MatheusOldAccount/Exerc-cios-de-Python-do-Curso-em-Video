from random import randint
computador = randint(0, 10)
tentativas = 0
jogador = 15
while jogador != computador:
    jogador = int(input('Digite o número que você acha que a máquina vai escolher: '))
    tentativas += 1
print('\033[35mVocê Ganhou na {}ª rodada(s), PARABÉNS ! Ambos escolheram o número {}\033[m'.format(tentativas, computador))
