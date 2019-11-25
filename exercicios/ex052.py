a = 0
num = int(input('Digite um número inteiro: '))
for i in range(2, 100000):
    if num % i == 0 and i != num:
        a = 1
if a == 0:
    print('O número é PRIMO')
else:
    print('O número não é PRIMO')
