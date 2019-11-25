n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vez(es)')
if tupla.count(3) > 0:
    print(f'O valor 3 apareceu na {tupla.index(3) +1}ª posição')
else:
    print(f'Não foi digitado nenhum valor 3')
print('Os valores pares digitados foi(ram): ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end='')
