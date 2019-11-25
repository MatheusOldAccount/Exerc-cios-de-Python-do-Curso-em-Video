num = int(input('Informe um número: '))
u = num // 1 % 10
#dividimos o numero por 1 e pegamos o resto da sua divisão por 10
#isso dará a unidade
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
#se fizemos c = num // 100 pegaríamos os 2 primeiros dígitos, mas como queremos só
#o segundo que representa a centena, pegamos o resto da divisão por 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
