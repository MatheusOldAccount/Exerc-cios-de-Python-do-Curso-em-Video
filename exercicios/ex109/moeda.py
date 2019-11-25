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
