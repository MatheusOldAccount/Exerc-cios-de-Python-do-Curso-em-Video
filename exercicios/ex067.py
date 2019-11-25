while True:
    print('-' * 40)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if tab < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{tab} * {cont} = {tab * cont}')
        cont += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
