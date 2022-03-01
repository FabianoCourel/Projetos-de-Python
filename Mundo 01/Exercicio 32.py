import random
import pygame
from time import sleep
x = random.randint(0, 5)
print('\033[33m--=\033[m'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('\033[33m--=\033[m'*20)
escolha = int(input('Em que número eu pensei?: '))
print('RUFEM OS TAMBORES...')
sleep(2)
if escolha == x:
    print('Parabéns, você \033[32mACERTOU\033[m o numero!')
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Acertou.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    print('Você \033[31mERROU\033[m o número que pensei!')
    print('O numero foi {} e não {}.'.format(x, escolha))
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Errou.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
