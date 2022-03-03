from datetime import date
ano = date.today().year
cadastro = {}
#Considerando que são 30 anos de contribuição para aposentar!
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Nascimento: '))
cadastro['Idade'] = ano - nasc
n = cadastro['Carteira de Trabalho'] = int(input('Número da carteira de trabalho'
                                              '\nCaso não houver registros preencha com 0: '))
if n != 0:
    x = cadastro['Ano de Contratação'] = int(input('Ano da 1a Contratação: '))
    apos = (x - nasc) + 30
    cadastro['Salário'] = float(input('Salário em Carteira: '))
    cadastro['Se aposenta com'] = apos
    print('')
    print('\033[33m-=\033[m' * 20)
else:
    print('')
    print('\033[33m-=\033[m' * 20)
for c, d in cadastro.items():
    print(f'{c}: {d}')