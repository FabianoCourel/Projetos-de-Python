n1 = float(input('Qual sua nota da primeira prova? '))
n2 = float(input('Qual sua nota da segunda prova? '))
M = (n1 + n2) / 2

if M < 5.0:
    print('Sua média foi: {:.1f}, você está \033[1;31mREPROVADO\033[m!'. format(M))
elif M > 6.9:
    print('Sua média foi: {:.1f}, você está \033[1;32mAPROVADO\033[m!' .format(M))
else:
    print('Sua média foi: {:.1f}, você está de \033[1;33mRECUPERAÇÃO\033[m!'.format(M))