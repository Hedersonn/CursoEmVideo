# Importar um MP3

import pygame

pygame.mixer.init()
pygame.mixer_music.load('Ex21.mp3')
pygame.mixer_music.play()
input()
pygame.quit()
