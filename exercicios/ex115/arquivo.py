def verPessoas():
    print('-' * 30)
    arq = open('lista.txt', 'r')
    print(arq.read())
    arq.close()


def adicionarPessoas():
    print('-' * 30)
    arq = open('lista.txt', 'a')
    nome = str(input('Nome: ')).strip().capitalize()
    válido = False
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado')
            arq.write(f'\n{nome:<30}{idade} anos')
            válido = True
        if válido:
            break
    arq.close()

