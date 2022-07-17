import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

# declare variables
width = 1600
height = 900

#set up the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wheel of Jeopardy")
clock = pygame.time.Clock()

background_1 = pygame.image.load('images/space_background.jpg').convert()
background_1 = pygame.transform.scale(background_1, (width, height))

#set up the colors
white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)

image  = pygame.image.load('images/space_background.jpg')

# text setting
rect_obj = pygame.draw.rect(background_1, blue, pygame.Rect(100, 100, 100, 100)) 
text_surface_object = pygame.font.SysFont('freesansbold.ttf', 32).render('my hello', True, green)
text_rect = text_surface_object.get_rect(center=rect_obj.center)

while True: # the main game loop
    # draw the text onto the surface
    screen.blit(background_1, (0, 0))
    screen.blit(text_surface_object, text_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)