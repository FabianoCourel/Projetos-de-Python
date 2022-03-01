soma = 0
cont = 0
print('Vou somar todos números ímpares de 1 a 500...')
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é de {}!' .format(cont, soma))