from random import randint
computador = 0
tentativas = 0
jogador = 15
while jogador != computador:
    computador = randint(0, 10)
    jogador = int(input('Digite o número que você acha que a máquina vai escolher: '))
    tentativas += 1
    if jogador != computador:
        print('\033[31mERROU ! O computador escolheu o número {} nessa rodada e você o número {}\033[m'.format(computador, jogador))
print('\033[35mVocê Ganhou na {}ª rodada(s), PARABÉNS ! Ambos escolheram o número {}\033[m'.format(tentativas, computador))
