tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
numero = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
while True:
    c = int(input('Digite um número de 0 a 10: '))
    if c in numero:
        break
print(f'Você digitou número {tupla[c]}')