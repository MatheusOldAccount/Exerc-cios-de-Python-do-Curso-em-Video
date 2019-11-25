from time import sleep


def contador(begin, end, step):
    if (begin > end >= 0) or (begin > end and end < 0):
        end -= 1
        step *= -1
    else:
        end += 1
    for d in range(begin, end, step):
        print(f'{d} ', end='')
        sleep(0.2)
    print('FIM!')


print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
    print(f'{c} ', end='')
    sleep(0.2)
print('FIM!')
print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -1, -2):
    print(f'{c} ', end='')
    sleep(0.2)
print('FIM!')
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 30)
if passo == 0:
    passo = 1
elif passo < 0:
    passo *= -1
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
contador(inicio, fim, passo)
