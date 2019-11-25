from time import sleep


def contador(inicio, fim, passo):
    if inicio < fim:
        if passo > 0:
            for d in range(inicio, fim + 1, passo):
                print(f'{d} ', end='')
                sleep(0.3)
            print('FIM!')
        else:
            for d in range(inicio, fim + 1, (passo * -1)):
                print(f'{d} ', end='')
                sleep(0.3)
            print('FIM!')
    else:
        if passo > 0:
            for d in range(inicio, fim - 1, (passo * -1)):
                print(f'{d} ', end='')
                sleep(0.3)
            print('FIM!')
        else:
            for d in range(inicio, fim - 1, passo):
                print(f'{d} ', end='')
                sleep(0.3)
            print('FIM!')


def linha():
    print('-=' * 30)


linha()
print('Contagem de 1 até 10 de 1 em 1 ')
for c in range(1, 11):
    print(f'{c} ', end='')
    sleep(0.3)
print('FIM!')
linha()
print('Contagem de 10 até 0 de 2 em 2 ')
for c in range(10, -1, -2):
    print(f'{c} ', end='')
    sleep(0.3)
print('FIM!')
linha()
print('Agora é sua vez de personalizar a contagem! ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
linha()
if p == 0:
    p = 1
if (i > f) and (p > 0):
    print(f'Contagem de {i} até {f} de {p} em {p} ')
elif (i > f) and (p < 0):
    print(f'Contagem de {i} até {f} de {p * -1} em {p * -1} ')
else:
    if (i < f) and (p > 0):
        print(f'Contagem de {i} até {f} de {p} em {p} ')
    elif (i > f) and (p < 0):
        print(f'Contagem de {i} até {f} de {p * -1} em {p * -1} ')
contador(i, f, p)
