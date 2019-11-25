soma = 0
qtde = 0
for count in range(0, 501, 3):
    if count % 2 != 0:
        soma += count
        qtde += 1
print('A soma de todos os {} valores solicitados é {}'.format(qtde, soma))
