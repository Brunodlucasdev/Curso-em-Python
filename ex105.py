def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas do aluno(aceita vaárias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação do aluno.
    :return: dicionário com várias informações sobre a turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


#Programa Principal
resp = notas(9.5, 9.5, 9, 9.5, sit=True)
print(resp)