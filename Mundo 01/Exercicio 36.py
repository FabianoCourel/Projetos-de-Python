from datetime import date
ano = int(input('Escolha um ano para vermos se é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 400 or ano % 400 == 0:
    print('O ano {} é bissexto!' .format(ano))
else:
    print('O ano {} não é bissexto!' .format(ano))