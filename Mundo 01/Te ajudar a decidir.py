import random
print('Esta em duvida no que escolher? Vou ajudar, diga três coisas que esta em duvida:')
n1 = str(input('[1]: '))
n2 = str(input('[2]: '))
n3 = str(input('[3]: '))
lista = (n1, n2, n3)
x = random.choice(lista)
print('Eu escolho por você a opção: {}' .format(x))