from time import sleep
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado a lista com sucesso!')
    else:
        print('Número repetido, não adicionado a lista...')
    x = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if 'N' in x:
        print('Registro encerrado, aguarde um instante...')
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        break
lista.sort()
print(f'A lista que você criou foi: {lista}')