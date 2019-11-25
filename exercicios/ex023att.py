num = int(input('Informe um número: '))
print('Analisando o número {}'.format(num))
numstr = str(num)
print('Unidade: {}'.format(numstr[len(numstr) - 1]))
if num < 10:
    print('Dezena : 0')
    print('Centena : 0')
    print('Milhar : 0')
else:
    if num < 100:
        print('Dezena: {}'.format(numstr[len(numstr) - 2]))
        print('Centena : 0')
        print('Milhar : 0')
    else:
        if num < 1000:
            print('Dezena: {}'.format(numstr[len(numstr) - 2]))
            print('Centena: {}'.format(numstr[len(numstr) - 3]))
            print('Milhar : 0')
        else:
            print('Dezena: {}'.format(numstr[len(numstr) - 2]))
            print('Centena: {}'.format(numstr[len(numstr) - 3]))
            print('Milhar: {}'.format(numstr[len(numstr) - 4]))
