resp = 'S'
tot = 0
soma = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    if tot == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    tot += 1
    soma += n
    resp = str(input('Você deseja continuar digitando valores? [S/N] ')).strip().replace(' ', '').upper()
media = soma / tot
print('A média entre todos os {} valores digitados é {:.2f}'.format(tot, media))
print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))
