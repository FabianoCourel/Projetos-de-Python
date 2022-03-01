from math import hypot
co = float(input('Qual tamanho do cateto oposto?'))
ca = float(input('Qual tamanho do cateto adjacente?'))
hipotenusa = hypot(co, ca)

print('o valor da hipotenusa do triangulo retangulo é: {:.2f}' .format(hipotenusa))