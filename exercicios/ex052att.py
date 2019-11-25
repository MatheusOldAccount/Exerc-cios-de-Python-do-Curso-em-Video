qtdenaoprimo = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        #NÃO É PRIMO
        print('\033[33m{}\033[m'.format(c), end=' ')
        qtdenaoprimo += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
if qtdenaoprimo > 2 or num == 1:
    print('\nO número {} foi divisível {} vezes\nE por isso ele NÃO É PRIMO!'.format(num, qtdenaoprimo))
else:
    print('\nO número {} foi divisível {} vezes\nE por isso ele É PRIMO!'.format(num, 2))
