# Reference: https://www.youtube.com/watch?v=_TU6BEyBieE

#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
from pygame.locals import *
import pygame
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

# make sure you provide your own image
img = pygame.image.load(r'images\wheel_revA.png').convert()
img.set_colorkey((0, 0, 0))

#angle = 0
# Loop ------------------------------------------------------- #
for angle in range(0, 180, 2):
    #angle += 2

    # Background --------------------------------------------- #
    screen.fill((0, 50, 0))

    mx, my = pygame.mouse.get_pos()
    img_copy = pygame.transform.rotate(img, angle)
    screen.blit(img_copy, (250 - int(img_copy.get_width() / 2),
                250 - int(img_copy.get_height() / 2)))
    # screen.blit(pygame.transform.rotate(img, angle), (250, 250))

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
