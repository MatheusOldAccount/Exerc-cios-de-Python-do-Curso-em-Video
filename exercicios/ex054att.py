from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = anoatual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoa(s) maiores de idade'.format(maior))
print('E também tivemos {} pessoa(s) menores de idade'.format(menor))
