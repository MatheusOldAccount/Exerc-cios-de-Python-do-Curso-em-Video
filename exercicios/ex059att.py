from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('{:^20}'.format('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'))
    escolha = int(input('>>>>> Qual é a sua opção? '))
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1*n2))
    elif escolha == 3:
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1)) if n1 > n2 else print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
    elif escolha == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif not escolha == 5:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre !')
