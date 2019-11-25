tot = soma = 0
while True:
    val = int(input('Digite um valor (999 para parar): '))
    if val == 999:
        break
    '''else: não precisa do else
        tot += 1
        soma += val'''
    tot += 1
    soma += val
print(f'A soma dos {tot} valores foi {soma}!')
