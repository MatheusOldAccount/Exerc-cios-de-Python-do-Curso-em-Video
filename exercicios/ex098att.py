from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            # Hoje não há mais esse problema, mas há um tempo atrás havia o problema em por o sleep que criava um flush de tela, não ia mostrando o número de tempo em tempo, esperava acabar tod o tempo aí mostrava tudo de uma vez, fazendo oque não queríamos. Para corrigir isso era só por no print depois do end, uma vírgula , e flush=False para tirar esse flush
            # Assim: print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
