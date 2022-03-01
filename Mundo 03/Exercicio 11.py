lista = []
impar = []
par = []
while True:
    numero = (int(input('Digite um valor: ')))
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    if numero % 2 == 1:
        impar.append(numero)
    x = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if x == 'N':
        break
    if x not in 'SN':
        print('\033[1;31mResposta invalida\033[m, responda corretamente se quiser encerrar o programa!')
print('\033[33m-=\033[m' * 30)
print(f'A lista completa dos números é: {lista}')
print(f'Os numeros pares foram: {par}')
print(f'Os números impares foram: {impar}')