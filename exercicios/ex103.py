def ficha(name='<desconhecido>', goals=0):
    return f'O jogador {name} fez {int(goals)} gol(s) no campeonato.'


print('-' * 30)
nome = str(input('Nome do Jogador: ')).strip().capitalize()
gols = str(input('Número de Gols: '))
while (not gols.isnumeric()) and len(gols) != 0:
    gols = str(input('Número de Gols: '))
if len(nome) == 0 and len(gols) != 0:
    print(ficha(goals=gols))
elif len(nome) != 0 and len(gols) != 0:
    print(ficha(nome, gols))
elif len(nome) == 0 and len(gols) == 0:
    print(ficha())
else:
    print(ficha(nome))
