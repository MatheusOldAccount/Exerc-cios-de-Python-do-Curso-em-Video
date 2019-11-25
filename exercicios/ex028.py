from random import randint
from time import sleep
#o método sleep faz o computador esperar, dormir por alguns segundos
num = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
escolha = int(input('Qual foi o número escolhido pelo computador? '))
print('PROCESSANDO...')
sleep(3)
#sleep(quantos segundos)
if escolha == num:
    print('Você Venceu')
else:
    print('Você Perdeu')
    print('O número que tinha sido escolhido pelo Computador era: {}'.format(num))
