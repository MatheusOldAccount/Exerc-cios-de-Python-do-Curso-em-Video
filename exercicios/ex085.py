lista = list()
even = list()#par
odd = []#ímpar
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
even.sort()
odd.sort()
lista.append(even[:])
lista.append(odd[:])
print('-=' * 30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
