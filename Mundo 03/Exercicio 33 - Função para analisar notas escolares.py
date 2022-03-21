def notas(*n, sit=False):
    """
    >> Função para analisar dados sobre as notas de um aluno.
    :param n: Varias Notas
    :param sit: (Opcional) Mostra a situação do aluno dependendo da sua media.
    :return: Dicionario com vários Dados.
    """

    r = {}
    r['Total de Notas'] = len(n)
    r['Maior Nota'] = max(n)
    r['Menor Nota'] = min(n)
    r["Media"] = sum(n) / len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Media'] >= 5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'

    return r

#Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
print()
#help(notas)