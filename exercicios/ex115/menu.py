def men():
    válid = False
    while True:
        print('-' * 30)
        print(f'{"MENU PRINCIPAL":^30}')
        print('-' * 30)
        print('\033[33m1 \033[m- \033[34mVer pessoas cadastradas \033[m')
        print('\033[33m2 \033[m- \033[34mCadastrar nova Pessoa \033[m')
        print('\033[33m3 \033[m- \033[34mSair do Sistema\033[m')
        print('-' * 30)
        try:
            opc = int(input('\033[33mSua Opção: \033[m'))
        except:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
        else:
            if 1 <= opc <= 3:
                válid = True
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
        if válid:
            break
    return opc

