def ficha(name='<desconhecido>', goals=0):
    return f'O jogador {name} fez {int(goals)} gol(s) no campeonato.'


# Programa Principal
print('-' * 30)
nome = str(input('Nome do Jogador: ')).strip().capitalize()
gols = str(input('Número de Gols: '))
if gols.isnumeric() and len(nome) > 0:
    print(ficha(nome, gols))
elif gols.isnumeric() and len(nome) == 0:
    print(ficha(goals=gols))
elif len(gols) == 0 and len(nome) > 0:
    print(ficha(nome))
else:
    print(ficha())
