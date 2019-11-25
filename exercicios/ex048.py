soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print('A soma entre todos esses números é {}'.format(soma))
