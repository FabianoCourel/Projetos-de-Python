from time import sleep
def contagem(a, b, c):
    print('\033[33m-=\033[m' * 22)
    if c >= 0:
        print(f'Contagem de {a} até {b} de {c} em {c}:')
    elif c < 0:
        print(f'Contagem de {a} até {b} de {c * -1} em {c * -1}:')
    if c == 0:
        c = 1
    if a > b and c > 0:
        c = c - (c*2)
    for c in range(a, b, c):
        sleep(0.4)
        print(c, end=' ')
    sleep(0.4)
    print(f'{b} FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('\033[33m-=\033[m' * 22)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)
