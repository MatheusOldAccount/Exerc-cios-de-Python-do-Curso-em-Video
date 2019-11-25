frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.upper().find('A') + 1))
print('A última letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))
#para procurar a última palavra A, é só por rfind, procurando da direita para esquerda

