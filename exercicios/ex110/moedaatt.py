from ex109 import moeda


def resumo(val, aumento, reducao):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda.metade(val, True):<8}')
    print(f'{"Dobro do preço:":<20}{moeda.dobro(val, True):<8}')
    print(f'{"Metade do Preço:":<20}{moeda.metade(val, True):<8}')
    print(f'{aumento}% de aumento:{"":<5}{moeda.aumentar(val, aumento, True):<8}')
    print(f'{reducao}% de redução:{"":<5}{moeda.diminuir(val, reducao, True):<8}')

