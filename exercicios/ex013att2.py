preço = float(input('Qual é o preço do produto? R$'))
avista = preço - (preço*10/100)
parcelado = preço + (preço * 8/100)
parcelas = int(input('Em quantas parcelas você deseja pagar? '))
n = parcelado / parcelas
print('O preço do produto normal é de R${:.2f}, a vista ele sai por R${:.2f}, e em {} parcelas o valor do produto passa a ser R${:.2f}, pagos em {} parcelas de R${:.2f} cada um.'.format(preço, avista, parcelas, parcelado, parcelas, n))
