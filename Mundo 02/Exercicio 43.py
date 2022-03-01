print('\033[33m-=-\033[m' * 12)
print('CRIAR LISTA DE COMPRAS E GASTOS')
print('\033[33m-=-\033[m' * 12)
barato = 999999999999999999999999999999
soma = 0
cont = 0
x = 'T'
while True:
    nome = str(input('Nome do Produto: ').title().strip())
    valor = float(input('Valor do produto: R$ '))
    soma = soma + valor
    if valor >= 1000:
        cont = cont + 1
    if valor < barato:
        barato = valor
        x = nome
    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja parar? [S/N]: ').upper().strip()[0]
    if parar == 'N':
        print('\033[33m-=-\033[m' * 12)
    if parar == 'S':
        break
print('\033[33m-=-\033[m' * 12)
print('Gasto Total: R${:.2f}' .format(soma))
print(f'''No total {cont} produtos custaram mais de R$1000,00
O produto mais barato da lista foi o {x}''')