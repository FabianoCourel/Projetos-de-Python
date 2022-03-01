import random
cont = 0
while True:
    print('\033[33m-=-\033[m' * 20)
    print('Vamos jogar par ou impar!')
    numero = int(input('Escolha um número: '))
    jogador = input('Par ou Impar? [P/I]: ').upper().strip()[0]
    computador = random.randint(0, 10)
    soma = computador + numero
    res = soma % 2
    if res == 0:
        print(f'Computador escolheu {computador} e você {numero}. O total é {soma}, portanto PAR.')
        if jogador != 'P':
            print(f'Você perdeu, escolheu ÍMPAR!')
            print('\033[33m-=-\033[m' * 20)
            break
        if jogador == 'P':
            cont = cont + 1
            print('Você venceu, vamos continuar!')
    if res == 1:
        print(f'Computador escolheu {computador} e você {numero}. O total é {soma}, portanto IMPAR.')
        if jogador != 'I':
            print('Você perdeu, escolheu PAR!')
            print('\033[33m-=-\033[m' * 20)
            break
        if jogador == 'I':
            cont = cont + 1
            print('Você venceu, vamos continuar!')
print(f'\033[31mGAME OVER\033[m, você venceu um total de {cont} vezes consecutivas até perder!')
