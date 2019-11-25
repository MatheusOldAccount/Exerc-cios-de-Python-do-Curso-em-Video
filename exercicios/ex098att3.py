from time import sleep


def contador(begin, end, step):
    print('-=' * 30)
    print(f'Contagem de {begin} até {end} de {step} em {step}')
    if begin > end:
        end -= 1
        step *= -1
    else:
        end += 1
    for d in range(begin, end, step):
        print(f'{d} ', end='')
        sleep(0.2)
    print('FIM!')


contador(1, 10, 1)
contador(10, -1, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
elif passo < 0:
    passo *= -1
contador(inicio, fim, passo)
