from time import sleep


def menu():
    print('-' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print('\033[1;33m1\033[m - \033[1;34mVer pessoas cadastradas\033[m')
    print('\033[1;33m2\033[m - \033[1;34mCadastrar nova Pessoa\033[m')
    print('\033[1;33m3\033[m - \033[1;34mSair do sistema\033[m')
    print('-' * 30)


def opc():
    while True:
        sleep(0.5)
        menu()
        while True:
            try:
                option = int(input('\033[1;33mSua opção: \033[m'))
            except (ValueError, TypeError):
                print('\033[31mErro: Por favor, digite um número inteiro válido.\033[m')
            except KeyboardInterrupt:
                print('\033[31mUsuário preferiu não informar os dados.\033[m')
            except Exception as erro:
                print(f'\033[31mErro: {erro.__cause__}\033[m')
            else:
                if option < 1 or option > 3:
                    print('\033[31mErro! Digite uma opção válida!\033[m')
                break
        if option == 1 or option == 2 or option == 3:
            break
    return option


def result():
    while True:
        tot = opc()
        if tot == 1:
            print('-' * 30)
            print(f'{"Opção 1":^30}')
            print('-' * 30)
        elif tot == 2:
            print('-' * 30)
            print(f'{"Opção 2":^30}')
            print('-' * 30)
        else:
            print('-' * 30)
            print(f'{"Saindo do sistema... Até logo!":^30}')
            print('-' * 30)
            break

