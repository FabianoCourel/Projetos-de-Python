print('-' * 22)
print('Sequencia de Fibonacci')
print('-' * 22)
t1 = 0
t2 = 1
cont = 2
termos = int(input('Quantos termos você quer mostrar? '))
print('{} → {} → ' .format(t1, t2), end='')
while cont < termos:
    t3 = t1 + t2
    print('{} → ' .format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('FIM')