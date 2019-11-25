import random
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
n = random.randint(1, 4)
print('O primeiro aluno recebe número 1, o segundo 2, o terceiro 3 e o quarto 4.\n O número sorteado foi: {}'.format(n))
if n == 1:
    (print('O aluno escolhido foi {}'.format(nome1)))
if n == 2:
    (print('O aluno escolhido foi {}'.format(nome2)))
if n == 3:
    (print('O aluno escolhido foi {}'.format(nome3)))
if n == 4:
    (print('O aluno escolhido foi {}'.format(nome4)))
