def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
    """
    grades = dict()
    grades['total'] = len(n)
    grades['maior'] = max(n)
    grades['menor'] = min(n)
    grades['média'] = (sum(n) / len(n))
    if sit:
        if grades['média'] >= 7:
            grades['situação'] = 'BOA'
        elif grades['média'] >= 5:
            grades['situação'] = 'RAZOÁVEL'
        else:
            grades['situação'] = 'RUIM'
    return grades


# Programa Principal
print('-' * 30)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
