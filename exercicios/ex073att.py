print('-='*30)
tupla = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Internacional', 'Athletico-PR', 'Botafogo',
         'Goiás', 'Corinthians', 'Grêmio', 'Bahia', 'Ceará', 'Fortaleza', 'Vasco', 'Cruzeiro', 'Fluminense',
         'Chapecoense', 'CSA', 'Avaí')
print(tupla)
print('-='*30)
print(f'Os 5 primeiros são {tupla[:5]}')
print('-='*30)
print(f'Os 4 últimos são {tupla[16:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(tupla)}')
print('-='*30)
print(f'O Chapecoense está na {tupla.index("Chapecoense") + 1}ª posição')
