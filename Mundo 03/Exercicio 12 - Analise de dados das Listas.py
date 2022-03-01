from time import sleep
lista = []
temp = []
cont = 0
pmaior = 0
pmenor = 99999999999999
while True:
    nome = (input('Digite um nome: '))
    temp.append(nome)
    cont += 1
    peso = (float(input('Digite um peso: ')))
    temp.append(peso)
    if peso > pmaior:
        pmaior = peso
    elif peso < pmenor:
        pmenor = peso
    lista.append(temp[:])
    temp.clear()
    x = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if x == 'N':
        print('Aguarde, encerrando programa e calculando resultados...')
        sleep(1)
        print('.', end=' ')
        sleep(1)
        print('.', end=' ')
        sleep(1)
        print('.')
        sleep(1)
        break
    if x not in 'SN':
        print('\033[31mResposta invalida\033[m, responda corretamente se desejar parar.')
print(f'Você cadastrou um total de {cont} pessoas')
print(f'O maior peso foi de {(pmaior):.2f} kg. Sendo este o peso de:', end=' ')
for p in lista:
    if p[1] == pmaior:
        print(f'{p[0]}', end='...')
print(f'\nO menor peso foi de {(pmenor):.2f} kg. Sendo este o peso de:', end=' ')
for t in lista:
    if t[1] == pmenor:
        print(f'{t[0]}', end='...')