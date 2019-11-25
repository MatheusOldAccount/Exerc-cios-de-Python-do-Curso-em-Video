num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = \033[31m{}\033[m'.format(num, c, (num * c)))
