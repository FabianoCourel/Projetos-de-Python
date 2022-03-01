matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição {l}, {c}: '))
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]
print('\033[33m-=\033[m' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{(matriz[l][c]): ^5}]', end='')
    print()
print('\033[33m-=\033[m' * 20)
print(f'A soma dos valores pares da matriz é: {soma}.')
print(f'A soma dos valores da terceira coluna são: {matriz[2][0] + matriz[2][1] + matriz [2][2]}.')
matriz[1].sort()
print(f'O maior valor da segunda fileira é: {matriz[1][2]}')