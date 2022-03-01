n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro número:'))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
p = n1 ** n2
print('A soma é {}, a subtração {}, a multiplicação é {},' .format(a, s, m))
print('A divisão é {:.3f}, já a divisão inteira {} e o resto da divisão é {},'.format(d, di, rd))
print('Enquanto a potencia é:', (p))