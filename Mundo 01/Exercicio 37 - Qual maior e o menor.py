num1 = int(input('Escolha o primeiro valor: '))
num2 = int(input('Escolha o segundo valor: '))
num3 = int(input('Escolha o terceiro valor: '))
if num1 > num2 > num3:
    print('O menor valor digitado foi {} e o maior foi {}!' .format(num3, num1))
if num3 > num2 > num1:
    print('O menor valor digitado foi {} e o maior foi {}!' .format(num1, num3))
if num2 > num3 > num1:
    print('O menor valor digitado foi {} e o maior foi {}!'.format(num1, num2))
if num2 > num1 > num3:
    print('O menor valor digitado foi {} e o maior foi {}!'.format(num3, num2))
if num1 > num3 > num2:
    print('O menor valor digitado foi {} e o maior foi {}!'.format(num2, num1))
if num3 > num1 > num2:
    print('O menor valor digitado foi {} e o maior foi {}!'.format(num2, num3))