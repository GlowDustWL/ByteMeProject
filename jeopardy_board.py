# Copied straight from Chris for test GUI setup

# import statements
from telnetlib import X3PAD
import pygame
from sys import exit
import button

# initialize pygame
pygame.init()

# initalize colors
dark_blue = (38, 54, 150)
light_purple = (190, 25, 207)
light_blue = (83, 239, 252)
color = (255,0,0)
color2 = (0, 255, 0)

# declare variables
width = 1600
height = 900

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wheel of Jeopardy")
clock = pygame.time.Clock()

# surfaces
background_1 = pygame.image.load('images/space_background.jpg').convert()
background_1 = pygame.transform.scale(background_1, (width, height))

# board box sizes
x_dim = 100
y_dim = 50

# board padding
x_pad = 10 
y_pad = 10

# title alignment
title_x_start = 900
title_y_start = 70
title_y_dim = y_dim + y_pad*2

# board alignment
full_x_start = 900
full_y_start = title_y_start + title_y_dim + 10
full_x_dim = x_dim*6+x_pad*(6+1)
full_y_dim = y_dim*5+y_pad*(5+1)
title_x_dim = full_x_dim

# main screen with jeopardy board in corner
def jeopardyBoard():
    while True:
        # draw elements
        screen.blit(background_1, (0, 0))
        # Draw title boxes
        pygame.draw.rect(background_1, dark_blue, pygame.Rect(title_x_start, title_y_start, title_x_dim, title_y_dim)) 
        for x in range (6):
            pygame.draw.rect(background_1, light_blue, pygame.Rect(title_x_start+x_pad+x_dim*x+x_pad*x, \
                        title_y_start+y_pad, x_dim, y_dim))\
            # self.screen.blit(self.font.render('hellooo', True, color, color))
        # Draw Big Board Rectangle
        pygame.draw.rect(background_1, dark_blue, pygame.Rect(full_x_start, full_y_start, full_x_dim, full_y_dim))        
        # Draw sub boxes
        for x in range (6):
            for y in range (5):
                pygame.draw.rect(background_1, light_blue, pygame.Rect(full_x_start+x_pad+x_dim*x+x_pad*x, \
                        full_y_start+y_pad+y_dim*y+y_pad*y, x_dim, y_dim))
        pygame.display.flip()       
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # update the game state
        pygame.display.update()
        clock.tick(60)

jeopardyBoard()
