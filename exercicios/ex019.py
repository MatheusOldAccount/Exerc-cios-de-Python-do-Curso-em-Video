from random import choice
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
#criamos uma lista adicionando a ela entre colchetes os valores ou variaveis que queremos
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
