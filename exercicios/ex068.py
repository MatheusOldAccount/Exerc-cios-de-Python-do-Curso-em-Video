tot = 0
from random import randint
while True:
    print('-='*20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*20)
    maquina = randint(0,10)
    pessoa = int(input('Diga um valor: '))
    parimpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    verifica = maquina + pessoa
    print('-' * 20)
    print(f'Você jogou {pessoa} e o computador {maquina}. Total de {verifica}', end=' ')
    if verifica % 2 == 0:
        print('DEU PAR')
        print('-' * 20)
        if parimpar == 'I':
            print('\033[31mVocê PERDEU!\033[m')
            break
        else:
            print('\033[32mVocê Venceu!\033[m')
            print('vamos jogar novamente...')
    else:
        print('DEU ÍMPAR')
        print('-' * 20)
        if parimpar == 'I':
            print('\033[32mVocê Venceu!\033[m')
            print('amos jogar novamente...')
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break
    tot += 1
print(f'GAME OVER! Você venceu {tot} vez(es).')
