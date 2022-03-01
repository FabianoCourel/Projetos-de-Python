import random
print('Sou seu computador. Vou pensar em um número de 0 a 10, será que você consegue adivinhar qual?')
computador = random.randint(0, 10)
acertou = False
palpites = 0
jogador = int(input('Qual o seu palpite? '))
while not acertou:
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            jogador = int(input('Um pouco menos. Qual seu palpite? '))
        elif jogador < computador:
            jogador = int(input('Um pouco mais. Qual seu palpite? '))
print('Acertou com {} tentativas!' .format(palpites))