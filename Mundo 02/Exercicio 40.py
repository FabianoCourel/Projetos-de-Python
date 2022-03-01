import random
while True:
    print('\033[33m-=-\033[m' * 20)
    print('''Vamos jogar par ou impar! Vou sortear um número de 0 a 10!
[0] Par
[1] Ímpar''')
    computador = random.randint(0, 10)
    jogador = int(input('Você quer par, ou ímpar? '))
    res = computador % 2
    if jogador != res:
        print(f'Você perdeu, o número sorteado foi {computador}, vamos de novo!')
    if jogador == res:
        break
print(f'O numero sorteado foi {computador}. Parabéns, você ganhou!')



