lista = []
cont = 0
while True:
    numero = (int(input('Digite um valor: ')))
    lista.append(numero)
    cont = cont + 1
    x = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if x == 'N':
        break
    if x not in 'SN':
        print('\033[1;31mResposta invalida\033[m, responda corretamente se quiser encerrar o programa!')
print('\033[33m-=\033[m' * 30)
print(f'Você digitou um total de {cont} números!')
lista.sort(reverse=True)
print(f'A lista que você criou em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')