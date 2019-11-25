def notas(*grades, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param grades: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    info = dict()
    info['total'] = len(grades)
    info['maior'] = max(grades)
    info['menor'] = min(grades)
    info['média'] = (sum(grades) / len(grades))
    if sit:
        if info['média'] >= 7:
            info['situação'] = 'BOA'
        elif info['média'] >= 5:
            info['situação'] = 'RAZOÁVEL'
        else:
            info['situação'] = 'RUIM'
    return info


print('-' * 30)
# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
# resp = notas(3.5, 10, 6.5, sit=True)
# resp = notas(3.2, 2, 6.5, 2, 7, 4, sit=True)
# resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
help(notas)
