# Test script for adding text 

import pygame
import sys
from sys import exit
from pygame.locals import *

# initialize pygame
pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wheel of Jeopardy")
clock = pygame.time.Clock()
# surfaces
background_1 = pygame.image.load('images/space_background.jpg').convert()
background_1 = pygame.transform.scale(background_1, (width, height))

# initalize colors
dark_blue = (38, 54, 150)
light_purple = (190, 25, 207)
light_blue = (83, 239, 252)

# setup jeopardy board dimensions
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

class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((white))
        pygame.display.update()


    def addRect(self, background_1, color):
        self.rect = pygame.draw.rect(background_1, color, (175, 75, 200, 100), 2)
        pygame.display.update()

    def addText(self):
        self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
        pygame.display.update()

# main screen with jeopardy board in corner
def jeopardyBoard():
    Pan3 = Pane()
    Pan3.addRect(background_1, light_blue)
    Pan3.addText()
    while True:
        # draw elements
        screen.blit(background_1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();

jeopardyBoard()