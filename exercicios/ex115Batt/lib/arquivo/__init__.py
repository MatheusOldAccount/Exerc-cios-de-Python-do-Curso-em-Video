from ex115Batt.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt é abrir o arquivo em modo read text, abrir ele como arquivo de texto tal qual é para ser
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # write text, escreve um arquivo de texto, e o + é para que caso o arquivo não exista ele seja criado
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
