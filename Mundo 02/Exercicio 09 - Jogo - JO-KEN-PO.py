import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
x = int(input('Qual sua jogada? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('\033[33m-=\033[m' *16)
print('Você escolheu {}!' .format(itens[x]))
print('O computador escolheu {}!' .format(itens[computador]))
if computador == 0: #Computador jogou Pedra
    if x == 0:
        print('\033[1;33mEMPATOU!\033[m')
    elif x == 1:
        print('VOCÊ \033[1;32mVENCEU!\033[m')
    elif x == 2:
        print('VOCÊ \033[1;31mPERDEU!\033[m')
    else:
        print('Jogada invalida!')
if computador == 1: #Computador jogou Papel
    if x == 1:
        print('\033[1;33mEMPATOU!\033[m')
    elif x == 2:
        print('VOCÊ \033[1;32mVENCEU!\033[m')
    elif x == 0:
        print('VOCÊ \033[1;31mPERDEU!\033[m')
    else:
        print('Jogada invalida!')
if computador == 2: #Computador jogou Tesoura
    if x == 2:
        print('\033[1;33mEMPATOU!\033[m')
    elif x == 0:
        print('VOCÊ \033[1;32mVENCEU!\033[m')
    elif x == 1:
        print('VOCÊ \033[1;31mPERDEU!\033[m')
    else:
        print('Jogada invalida!')
print('\033[33m-=\033[m' *16)