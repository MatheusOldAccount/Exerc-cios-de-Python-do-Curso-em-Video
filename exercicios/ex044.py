preço = float(input('Preço do produto: R$'))
condição = int(input('Qual forma deseja pagar?\n[1] = À vista\n[2] = À vista no cartão\n[3] = Em até 2x no cartão\n[4] = 3x Ou mais?\n'))
if condição == 4:
    parcelas = int(input('Em quantas vezes você deseja pagar? '))
    if parcelas < 3:
        print('Não é possível pagar em menos de 3 vezes nessa operação')
    else:
        print('O valor final será de R${:.2f}, pagos em {} parcelas de R${:.2f} cada uma.'.format((preço + preço * 0.2), parcelas, ((preço + preço * 0.2) / parcelas)))
elif condição == 3:
    print('O valor final será de R${:.2f}, pagos em 2 vezes de R${} cada uma.'.format(preço, preço / 2))
elif condição == 2:
    print('O valor final será de R${:.2f}.'.format(preço - (preço * 5/100)))
elif condição == 1:
    print('O valor final será de R${:.2f}.'.format(preço - (preço * 10/100)))
else:
    print('Condição escolhida inexistente.')
