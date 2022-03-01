import random
aluno1=input('Escolha um nome:')
aluno2=input('Escolha um nome:')
aluno3=input('Escolha um nome:')
aluno4=input('Escolha um nome:')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação do trabalho será:')
print(lista)