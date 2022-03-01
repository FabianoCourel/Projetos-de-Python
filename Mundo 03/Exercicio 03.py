import random
a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)
e = random.randint(0, 10)
tupla = (a, b, c, d, e)
print(f'Os números sorteados foram: {tupla}')
x = sorted(tupla)
print(f'O MENOR número sorteado foi o: {x[0]}')
print(f'O MAIOR número sorteado foi o: {x[4]}')

print('\nDe novo:')

sorteio = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
           random.randint(0, 10), random.randint(0, 10))
print(f'\nOs números sorteados foram: {sorteio}')
print(f'O MENOR número sorteado foi o: {min(sorteio)}')
print(f'O MAIOR número sorteado foi o: {max(sorteio)}')