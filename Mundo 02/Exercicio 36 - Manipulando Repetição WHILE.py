c = 0
cont = 0
soma = 0
while c < 999:
    c = int(input('Digite um número [Digite 999 para parar]: '))
    if c < 999:
        soma = soma + c
        cont = cont + 1
print('Você digitou {} números, a soma deles foi: {}' .format(cont, soma))