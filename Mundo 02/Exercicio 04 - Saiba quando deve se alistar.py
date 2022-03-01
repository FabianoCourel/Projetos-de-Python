from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
serv = atual - ano

if serv > 18:
    print('Você ja passou da idade de servir o exercito!')
elif serv < 18:
    rest = 18 - serv
    print('Você ainda vai servir o exercito daqui {} anos!' .format(rest))
else:
    print('Você está na idade de servir ao exercito!')