dados = {}
lista = []
tot = 0
n = dados['Nome:'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {n} jogou: '))
for p in range(0, partidas):
    lista.append(int(input(f'   Quantos gols na {p+1}a partida: ')))
dados['Gols:'] = lista
soma = sum(lista)
dados['Total de Gols:'] = soma
print('')
print('\033[33m-=\033[m' * 50)
print(dados)
print('\033[33m-=\033[m' * 50)
for d, j in dados.items():
    print(f'{d} {j}')
print('\033[33m-=\033[m' * 50)
print(f'O jogador {n} jogou {partidas} partidas.')
for j, g in enumerate(lista):
    print(f'    → Na partida {j+1}, fez {g} gols')