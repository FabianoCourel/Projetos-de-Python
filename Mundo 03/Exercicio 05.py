lista = ('Pão', 2.50, 'Manteiga', 4.80, 'Mortadela', 4.45, 'Café', 3.50)
print('\033[33m-=-\033[m' * 10)
print(f'{"LISTA DE PREÇOS":^30}')
print('\033[33m-=-\033[m' * 10)
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end=' ')
    else:
        print(f'R$ {lista[pos]:>2.2f}')
