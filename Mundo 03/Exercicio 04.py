num = ( int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')) )
print(f'\nO número 9 apareceu um total de {num.count(9)} vezes!')
if 3 in num:
    print(f'O número 3 apareceu a primeira vez na posição: {num.index(3)+1}')
else:
    print('Você não digitou o número 3!')
print(f'Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')
