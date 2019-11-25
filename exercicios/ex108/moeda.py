def aumentar(preco, porcent):
    return preco + (preco * porcent / 100)


def diminuir(preco, porcent):
    return preco - (preco * porcent / 100)


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2


def moeda(func):
    var = f'{func:.2f}'
    return f'R${var.replace(".",",")}'
