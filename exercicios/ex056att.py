totidade = 0
hmaisvelho = 0
contm = 0
for c in range(1, 5):
    #print('-' * 5, ' {}ª PESSOA '.format(c), '-' * 5)
    print('{:-^20}'.format(' {}ª PESSOA ').format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    totidade += idade
    if sexo == 'M':
        if idade > hmaisvelho:
            hmaisvelho = idade
            nmaisvelho = nome
    elif sexo == 'F':
        if idade < 20:
            contm += 1
    else:
        print('Sexo inválido')
mediaidade = totidade / 4
print('A média de idade do grupo é de {:.1f} ano(s)'.format(mediaidade))
if hmaisvelho == 0:
    print('Não foi digitado nenhum homem.')
else:
    print('O homem mais velho tem {} ano(s) e se chama {}.'.format(hmaisvelho, nmaisvelho))
if contm == 0:
    print('Não há nenhuma mulher com menos de 20 anos')
else:
    print('Ao todo é(são) {} mulher(es) com menos de 20 anos'.format(contm))
