np1 = float(input('Digite a sua primeira nota: '))
np2 = float(input('Digite a sua segunda nota: '))
média = (np1+np2) / 2
if média <= 5:
    print('Média: {:.1f}\nREPROVADO'.format(média))
elif média < 7:
    print('Média: {:.1f}\nRECUPERAÇÃO'.format(média))
else:
    print('Média: {:.1f}\nAPROVADO'.format(média))
