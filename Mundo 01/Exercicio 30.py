Nome = input('Digite seu nome completo: ').split()
print('Muito prazer em te conhecer, {}!' .format(Nome[1]))
print('Seu primeiro nome é: {}' .format(Nome[0]))
print('Seu ultimo nome é: {}' .format(Nome[len(Nome)-1]))
