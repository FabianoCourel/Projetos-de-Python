tempo = int(input('Qual a sua idade? '))
if tempo <=45:
    print('Você é novo(a) ainda!')
else:
    print('Ta velho(a), hein?')

n1 = float(input('Qual sua nota da primeira prova? '))
n2 = float(input('Qual sua nota da segunda prova? '))
m = (n1 + n2) / 2
print('Sua media foi {:.1f}' .format(m))
if m >= 7:
    print('Parabéns, você está \033[32maprovado(a)\033[m!')
else:
    print('Você \033[31mreprovou\033[m, estude mais!')