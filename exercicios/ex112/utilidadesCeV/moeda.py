def aumentar(preco, porcent, var=False):
    result = preco + (preco * porcent / 100)
    if var:
        return moeda(result)
    else:
        return result


def diminuir(preco, porcent, var=False):
    result = preco - (preco * porcent / 100)
    if var:
        return moeda(result)
    else:
        return result


def dobro(preco, var=False):
    result = preco * 2
    if var:
        return moeda(result)
    else:
        return result


def metade(preco, var=False):
    result = preco / 2
    if var:
        return moeda(result)
    else:
        return result


def moeda(func):
    resp = f'{func:.2f}'
    return f'R${resp.replace(".",",")}'


def resumo(val, aumento, reducao):
    valor = f'{val:.2f}'
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}R${valor.replace(".", ",")}')
    print(f'{"Dobro do preço:":<20}{dobro(val, True):<8}')
    print(f'{"Metade do Preço:":<20}{metade(val, True):<8}')
    print(f'{aumento}% de aumento:{"":<5}{aumentar(val, aumento, True):<8}')
    print(f'{reducao}% de redução:{"":<5}{diminuir(val, reducao, True):<8}')

