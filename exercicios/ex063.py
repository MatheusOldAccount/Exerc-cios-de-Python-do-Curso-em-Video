n = int(input('Quantos valores da sequência fibonnacci você deseja ver? '))
a = 0
b = 1
if n >= 1:
    print(a, end=' -> ')
if n >= 2:
    print(b, end=' -> ')
cont = 2
while cont < n:
    c = a + b
    print(c, end=' -> ')
    a = b
    b = c
    cont += 1
print('Acabou')
