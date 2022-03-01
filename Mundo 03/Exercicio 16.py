import random
lista = []
jogos = []
cont = 0
tot = 0
print('-' * 50)
print(f"{'JOGA NA MEGA SENA': ^50}")
print('-' * 50)
x = int(input('Quantos jogos você deseja que eu sorteie? '))
print()
print(f'-=-=-=- < SORTEANDO {x} JOGOS > -=-=-=-')
print()
while tot < x:
    cont = 0
    while True:
        mega = random.randint(0, 60)
        if mega not in lista:
            lista.append(mega)
            cont = cont + 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
for c, v in enumerate(jogos):
    print(f'Jogo {c+1}: {v}')
print()
print(f'-=-=-=-=-=- < BOA SORTE > -=-=-=-=-=-')

