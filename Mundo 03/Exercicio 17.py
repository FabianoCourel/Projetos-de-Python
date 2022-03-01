from time import sleep
lista = []
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if continuar not in 'SN':
        print('Dado \033[31mINVALIDO\033[m, digite corretamente para parar!')
    if continuar == 'N':
        break
print()
print('\033[33m-=\033[m' * 20)
print()
print(f"{'No.':<4} {'Nome:':<10} {'Media:':>8}")
print('-' * 25)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 25)
    x = int(input('Qual No. do aluno que deseja ver as notas? [999 para parar]: '))
    if x == 999:
        print('Finalizando', end='')
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        break
    if x <= len(lista)-1:
        print(f'Notas de {lista[x][0]} são: {lista[x][1]}')
print('< PROGRAMA ENCERRADO >')


