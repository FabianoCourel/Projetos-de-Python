Nome = (input('Qual seu nome completo? '))
print('Nome todo maiusculo:', Nome.upper())
print('Nome todo minusculo:', Nome.lower())
espacos = Nome.count(' ')
x = len(Nome)
print('O nome completo possui {} letras' .format(x-espacos))
y = Nome.split()
print('Seu primeiro nome possui {}' .format(len(y[0])))
print('Seu segundo nome possui {}' .format(len(y[1])))