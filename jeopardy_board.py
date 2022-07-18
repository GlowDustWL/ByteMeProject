# Copied straight from Chris for test GUI setup

# import statements
import pygame
from sys import exit

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

# full board size
full_x_dim = 600
full_y_dim = 480

# board padding
x_pad = 10 
y_pad = 10

# board box sizes
x_dim = (full_x_dim - x_pad*7)/6
y_dim = (full_y_dim - y_pad*6)/5

# title alignment
title_x_start = 900
title_y_start = 70
title_y_dim = y_dim + y_pad*2

# board alignment
full_x_start = 900
full_y_start = title_y_start + title_y_dim + 10
title_x_dim = full_x_dim

# title boxes
categories = ['will', 'libby', 'chris', 'joe', 'mich', 'xyz']
# Dollar amount boxes
dollar = ['$200', '$400', '$600', '$800', '$1000']

# main screen with jeopardy board in corner
def jeopardyBoard():
    while True:
        # draw elements
        screen.blit(background_1, (0, 0))
        # Draw title boxes
        pygame.draw.rect(background_1, dark_blue, pygame.Rect(title_x_start, title_y_start, title_x_dim, title_y_dim)) 
        for x in range (6):
            # Draw Big Board Rectangle
            rect_obj = pygame.draw.rect(background_1, light_blue, pygame.Rect(title_x_start+x_pad+x_dim*x+x_pad*x, \
                        title_y_start+y_pad, x_dim, y_dim))
            text_surface_object = pygame.font.SysFont('freesansbold.ttf', 32).render(categories[x], True, light_purple)
            text_rect = text_surface_object.get_rect(center=rect_obj.center)
            screen.blit(text_surface_object, text_rect)       
        # Draw sub boxes
        pygame.draw.rect(background_1, dark_blue, pygame.Rect(full_x_start, full_y_start, full_x_dim, full_y_dim)) 
        for x in range (6):
            for y in range (5):
                rect_obj = pygame.draw.rect(background_1, light_blue, pygame.Rect(title_x_start+x_pad+x_dim*x+x_pad*x, \
                        title_y_start+y_pad+y_dim*y+y_pad*y+y_dim+3*y_pad, x_dim, y_dim))
                text_surface_object = pygame.font.SysFont('freesansbold.ttf', 32).render(dollar[y], True, light_purple)
                text_rect = text_surface_object.get_rect(center=rect_obj.center)
                screen.blit(text_surface_object, text_rect)
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
