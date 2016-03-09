import pygame,sys
from pygame.locals import *

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.display.set_caption('Hello world!')

screen = pygame.display.set_mode((500, 500))
myfont = pygame.font.SysFont("monospace", 15)
text = myfont.render('HelloOOOOO world!', True, BLACK , WHITE)
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery
screen.fill(WHITE)
screen.blit(text,textRect)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()