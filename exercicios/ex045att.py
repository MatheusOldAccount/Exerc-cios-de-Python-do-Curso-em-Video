from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opção = int(input('Qual é a sua jogada? '))
maquina = randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if opção == maquina == 0:
    pc = 'Pedra'
    j1 = 'Pedra'
    vencedor = 'NINGUÉM'
elif opção == maquina == 1:
    pc = 'Papel'
    j1 = 'Papel'
    vencedor = 'NINGUÉM'
elif opção == maquina == 2:
    pc = 'Tesoura'
    j1 = 'Tesoura'
    vencedor = 'NINGUÉM'
elif opção == 0 and maquina == 1:
    pc = 'Papel'
    j1 = 'Pedra'
    vencedor = 'MÁQUINA'
elif opção == 0 and maquina == 2:
    pc = 'Tesoura'
    j1 = 'Pedra'
    vencedor = 'JOGADOR'
elif opção == 1 and maquina == 0:
    pc = 'Pedra'
    j1 = 'Papel'
    vencedor = 'JOGADOR'
elif opção == 1 and maquina == 2:
    pc = 'Tesoura'
    j1 = 'Papel'
    vencedor = 'MÁQUINA'
elif opção == 2 and maquina == 0:
    pc = 'Pedra'
    j1 = 'Tesoura'
    vencedor = 'MÁQUINA'
elif opção == 2 and maquina == 1:
    pc = 'Papel'
    j1 = 'Tesoura'
    vencedor = 'JOGADOR'
print('-=' * 20)
print('Computador jogou {}'.format(pc))
print('Jogador jogou {}'.format(j1))
print('-=' * 20)
print('{} VENCE'.format(vencedor))
