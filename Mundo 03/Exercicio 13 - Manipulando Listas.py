num = [[], []]
for c in range(1, 8):
    x = int(input(f'Digite o {c}o valor: '))
    if x % 2 == 0:
        num[0].append(x)
    if x % 2 == 1:
        num[1].append(x)
num[0].sort()
print(f'Os números pares escolhidos são: {num[0]}')
num[1].sort()
print(f'Os números impares escolhidos são: {num[1]}')
