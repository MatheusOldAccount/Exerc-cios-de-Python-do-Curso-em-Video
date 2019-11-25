termo = int(input('Quantos termos você quer mostrar?'))
a = 0
b = 1
print(f'{a} -> {b}', end='')
while termo > 0:
    c = a + b
    print(f' -> {c}', end='')
    a = b
    b = c
    termo -= 1
