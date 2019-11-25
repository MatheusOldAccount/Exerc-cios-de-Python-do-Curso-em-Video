maioridade = 0
menoridade = 0
from datetime import date
anoatual = date.today().year
for c in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento: '))
    if anoatual - nasc < 22:
        menoridade += 1
    else:
        maioridade += 1
print('{} pessoa(s) atingiu(ram) a Maioridade.'.format(maioridade))
print('{} pessoa(s) ainda não atingiu(ram) a Maioridade.'.format(menoridade))
