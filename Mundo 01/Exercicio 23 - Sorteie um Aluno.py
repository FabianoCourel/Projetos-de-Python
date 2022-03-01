import random
aluno1=input('Escolha um nome')
aluno2=input('Escolha um nome')
aluno3=input('Escolha um nome')
aluno4=input('Escolha um nome')
num = random.choice((aluno1, aluno2, aluno3, aluno4))
print('O aluno que ira apagar o quadro será o(a): {}' .format(num))