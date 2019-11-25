v0 = int(input('Digite um número: '))
v1 = int(input('Digite outro número: '))
v2 = int(input('Digite mais um número: '))
v3 = int(input('Digite o último número: '))
tupla = v0, v1, v2, v3
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vez(s)')
if tupla.count(3) > 0:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
qtde = 0
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        qtde += 1
if qtde > 0:
    print('O(s) valor(es) par(es) digitado(s) foi(foram)', end=' ')
    for c in range(0, 4):
        if tupla[c] % 2 == 0:
            print(f'{tupla[c]}', end=' ')
else:
    print('Não houveram valores pares digitados')
