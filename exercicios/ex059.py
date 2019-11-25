from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
escolha = 10
while escolha != 5:
    print('''{:^20}
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa'''.format('MENU'))
    escolha = int(input('Oque deseja fazer? '))
    if escolha == 1:
        print('A soma de {} com {} é {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('A multiplicação de {} com {} é {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        print('O maior valor digitado é {}'.format(n1)) if n1 > n2 else print('O maior valor digitado é {}'.format(n2))
    elif escolha == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif escolha == 5:
        print('Saindo do programa ... ')
        sleep(3)
    else:
        print('Solicitação inválida. Favor, verificar menu e digitar opção novamente.')
