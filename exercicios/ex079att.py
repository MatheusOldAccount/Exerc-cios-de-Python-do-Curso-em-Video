lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar')
    proceed = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if proceed == 'N':
        break
print('-='*30)
lista.sort()
print(f'Você digitou os valores {lista}')
