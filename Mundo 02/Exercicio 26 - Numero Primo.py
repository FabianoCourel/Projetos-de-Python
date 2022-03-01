num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), end=' ')
print('\033[m!')
print('O número {} foi divisível \033[33m{} vezes\033[m' .format(num, tot))
if tot == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO é primo!')