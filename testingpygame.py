
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')

white = (255,255,255)

pygame.draw.rect(DISPLAYSURF,white,(100,100,100,50))

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        pygame.display.update()
