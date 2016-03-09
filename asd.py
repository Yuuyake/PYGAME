import pygame, sys
import time

pygame.init()

padimage = pygame.image.load("pad.png")
window = pygame.display.set_mode((1000, 1000))
backg = pygame.image.load("backg.jpg")

while 1:
    window.blit(backg, (0, 0))

        window.blit(padimage, (400, 400))

pygame.quit()
