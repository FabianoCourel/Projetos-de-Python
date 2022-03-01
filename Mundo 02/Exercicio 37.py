n = int(input('Digite um número: '))
x = input('Deseja parar? [S/N]: ').upper().strip()
cont = 1
soma = n
media = 0
maior = 0
menor = n
while x == "N":
    n = int(input('Digite um número: '))
    x = input('Deseja parar? [S/N]: ').upper().strip()
    cont = cont + 1
    soma = soma + n
    media = soma / cont
    if n >= maior:
        maior = n
    if n < menor:
        menor = n
if x not in 'SN':
    print('Dado invalido, feche o programa e comece do zero.')
print('Você digitou {} números, a média deles foi {}' .format(cont, media))
print('O maior valor foi {} e o menor foi {}!' .format(maior, menor))