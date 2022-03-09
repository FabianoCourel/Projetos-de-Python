dados = {}
gols = []
lista = []
tot = 0
while True:
    gols.clear()
    n = dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {n} jogou: '))
    for p in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na {p+1}a partida: ')))
    dados['Gols'] = gols[:]
    soma = sum(gols)
    dados['Total de Gols'] = soma
    lista.append(dados.copy())
    parar = str(input('Deseja parar? [S/N]: ')).upper().strip()[0]
    while parar not in 'SN':
        print('Resposta \033[31mINVALIDA\033[m')
        parar = str(input('Deseja parar? [S/N]')).upper().strip()[0]
    if parar == 'S':
        break
print('')
print('\033[33m-=\033[m' * 20)
print('-' * 30)
print(f'{"Cod.":>4} {"Nome":<3} {"Gols":>9} {"Total":>8}')
print('-' * 30)
for k, v in enumerate(lista):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<10}', end='')
    print()
print('-' * 30)
print('\033[33m-=\033[m' * 20)
while True:
    x = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if x == 999:
        break
    if x >= len(lista):
        print(f'    > Não existe jogador com codigo {x} <')
        print('-' * 52)
    else:
        print(f' -- Levantamento do jogador {lista[x]["Nome"]}: --')
        for i, g in enumerate(lista[x]['Gols']):
            print(f'        > No jogo {i+1} fez {g} gols!')
        print('-' * 52)
print('PROGRAMA ENCERRADO'
      '\n< VOLTE SEMPRE >')