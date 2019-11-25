from time import sleep


def maior(*numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')
    tam = len(numeros)
    # NÃO É NECESSÁRIO USAR ESSE tam POIS CONSEGUIMOS USAR O MÉTODO len PARA numeros MESMO SE NÃO FOR PASSADO NENHUM PARÂMETRO, POIS ASSIM SERÁ CRIADO UMA TUPLA VAZIA NO QUAL FUNCIONA O len
    if tam > 0:
        for c in numeros:
            print(f'{c} ', end='')
            sleep(0.3)
        maximo = max(numeros)
    else:
        tam = maximo = 0
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maximo}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
