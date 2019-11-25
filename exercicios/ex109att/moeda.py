def aumentar(preço=0, taxa=0, formato=False):
    # É recomendável criar as docstrings p/ fazermos interactive help pois quando modularizamos as coisas ocultamos o código, oque é bom, enquanto o interactive help serve para deixar bem explicito oque foi ocultado
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)
# Não precisamos colocar o nome do módulo em moeda(preço) porque já está no mesmo módulo
# OBS: precisamos substituir o == pelo operador is porque se trata de True/False, ou not format


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, mo='R$'):
    return f'{mo}{preço:>.2f}'.replace('.', ',')
