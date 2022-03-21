def ficha(a, b):
    if a == '':
        a = '< Desconhecido >'
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')

nome = input('Nome do Jogador: ')
gols = input('Quantos gols ele marcou? ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
