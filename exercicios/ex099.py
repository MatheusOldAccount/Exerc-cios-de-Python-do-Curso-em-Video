from time import sleep


def maior(*arg):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in arg:
        print(f'{c} ', end='')
        sleep(0.3)
    print(f'Foram informados {len(arg)} valores ao todo.')
    if len(arg) == 0:
        big = 0
    else:
        big = max(arg)
    print(f'O maior valor informado foi {big}.\n')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
