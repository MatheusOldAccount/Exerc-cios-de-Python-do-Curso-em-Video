np1 = float(input('Primeira nota: '))
np2 = float(input('Segunda nota: '))
media = (np1 + np2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(np1, np2, media))
if media < 5:
    print('O aluno está REPROVADO.')
elif media < 6.9:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
