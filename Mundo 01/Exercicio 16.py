valor = float(input('Quanto custa determinado produto? R$'))
calc = valor/100
desc = calc*5
custo = valor-desc
print('Com desconto de 5%, seu produto de R${} custará R${}'.format(valor, custo))
print('-'*60)
pret = float(input('Qual % de desconto você deseja?'))
r = calc*pret
print('O produto que custa R${}, passará a valer R${} com {}% de desconto'.format(valor, valor*pret/100, pret))