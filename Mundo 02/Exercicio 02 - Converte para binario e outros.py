num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:'
[1] Converter para BINÁRIO
[2] Converter para OCTAL 
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a: {}.' .format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a: {}.' .format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}.' .format(num, hex(num)))
else:
    print('-Valor invalido-')