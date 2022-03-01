import random
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': random.randint(1, 6),
          'jogador2': random.randint(1, 6),
          'jogador3': random.randint(1, 6),
          'jogador4': random.randint(1, 6)}
ranking = []
print('Valores Sorteados:')
for j, d in jogadores.items():
     print(f'  O {j} tirou {d} no dado!')
     sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('')
print('\033[33m-=\033[m' * 20)
print('')
print('Ranking dos Jogadores:')
for r, j in enumerate(ranking):
     print(f'  O {r+1}o Colocado: {j[0]} com {j[1]}.')
     sleep(1)
