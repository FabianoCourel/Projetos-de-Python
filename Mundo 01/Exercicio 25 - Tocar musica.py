import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('FF7.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#Para funcionar, deverá na mesma pasta possuir arquivo de mp3 renomeado igual ao que programar