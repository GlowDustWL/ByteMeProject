# import statements
import pygame
import math


class Wheel:

    def __init__(self):
        # initalize colors
        self.dark_blue = (38, 54, 150)
        self.light_purple = (190, 25, 207)
        self.light_blue = (83, 239, 252)
        self.color = (255, 0, 0)
        self.color2 = (0, 255, 0)
        self.white = (255, 255, 255)

        self.x_y_center = (350,250)
        self.radius = 190

        self.sections = ["lose", "free", "bankrupt", "player's choice", "opponents", "spin again",
                        "cat 1", "cat 2", "cat 3", "cat 4", "cat 5", "cat 6"]

    def draw(self, surface):

        # get mouse position
        pos = pygame.mouse.get_pos()

        # circle
        pygame.draw.circle(surface, self.light_blue, self.x_y_center, self.radius)

        # draw lines
        start_pos = self.x_y_center
        # trig
        for i in range(12):
            x_add = self.radius*math.cos(30*i*math.pi/180)
            y_add = self.radius*math.sin(30*i*math.pi/180)
            end_pos = (350+x_add, 250+y_add)
            pygame.draw.line(surface, self.white, start_pos, end_pos, width = 3)

        for i in range(1):
         # adding text
            font = pygame.font.SysFont('freesansbold.ttf', 32)
            text_surface_object = font.render(self.sections[i], True, self.light_purple)
            angle_change = -15-(i*30)
            text_surface_object = pygame.transform.rotate(text_surface_object, angle_change)
            x_add = self.radius/2*math.cos(15*(i+1)*math.pi/180)
            y_add = self.radius/2*math.sin(15*(i+1)*math.pi/180)
            end_pos = (350+x_add, 250+y_add)
            surface.blit(text_surface_object, end_pos)
            
        pygame.display.flip()
