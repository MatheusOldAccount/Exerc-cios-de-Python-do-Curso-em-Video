'''print('=' * 11, end=' ')
print('LOJAS MATHEUS', end=' ')
print('=' * 11)'''
print('{:=^40}'.format(' LOJAS MATHEUS '))
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    preçofinal = preço - (preço * (10/100))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preçofinal))
elif opção == 2:
    preçofinal = preço - (preço * (5 / 100))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preçofinal))
elif opção == 3:
    preçofinal = preço
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preço / 2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preçofinal))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    valorcomjuros = (preço + (preço * 20 / 100))
    valorparcelas = valorcomjuros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, valorparcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, valorcomjuros))
else:
    print('Opção inválida !')
