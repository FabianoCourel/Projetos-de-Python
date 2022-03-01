dicionario = {}
dicionario['Nome'] = input('Qual nome do aluno? ')
dicionario['Media'] = float(input('Qual sua media? '))
if dicionario['Media'] >= 7:
    dicionario['Situação'] = '\033[32mAPROVADO\033[m'
elif 5 <= dicionario['Media'] < 7:
    dicionario['Situação'] = '\033[33mRECUPERAÇÃO\033[m'
else:
    dicionario['Situação'] = '\033[31mREPROVADO\033[m'
print('')
print('\033[33m-=\033[m' * 20)
for n, m in dicionario.items():
    print(f'{n} é igual a {m}')