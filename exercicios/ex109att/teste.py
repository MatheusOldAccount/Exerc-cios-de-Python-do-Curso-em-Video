from ex109att import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p, "US$")} é {moeda.metade(p, True)}')
# Esse True representa o formatado, é oque faz com que seja formatado passando pela função moeda do módulo moeda
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
