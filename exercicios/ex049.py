num = int(input('Digite o número que você deseja ver a tabuada: '))
for c in range(1, 11):
    print('{:2} * {} = {}'.format(c, num, (c * num)))
print('FIM')
