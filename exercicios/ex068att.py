from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
win = 0
while True:
    pc = randint(0, 10)
    val = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*30)
    soma = pc + val
    print(f'Você jogou {val} e o computador {pc}. Total de {soma}', end=' ')
    if soma % 2 == 0:
        print('DEU PAR')
        print('-' * 30)
        if pi == 'P':
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=-' * 30)
            win += 1
        else:
            print('Você PERDEU!')
            print('=-' * 30)
            break
    else:
        print('DEU ÍMPAR')
        print('-' * 30)
        if pi == 'I':
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=-' * 30)
            win += 1
        else:
            print('Você PERDEU!')
            print('=-' * 30)
            break
print(f'GAME OVER! Você venceu {win} vez(es).')
