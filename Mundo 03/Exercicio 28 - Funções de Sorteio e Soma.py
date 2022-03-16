import random
from time import sleep
lista = []
tot = 0
def sorteio(numeros):
    print('SORTEANDO 5 VALORES DA LISTA:')
    print('   > ', end='')
    for c in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n} - ', end='')
        sleep(0.4)
    print('Pronto!')
def soma(numeros):
    print('SOMANDO SOMENTE OS NUMEROS PARES DA LISTA:')
    sleep(1)
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma = soma + v
    print(f'   Total: {soma}.')

sorteio(lista)
print()
soma(lista)