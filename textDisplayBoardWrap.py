import pygame
from pygame.locals import *


class Pane:
    def __init__(self, fontSize):
        self.light_purple = (190, 25, 207)
        self.light_blue = (83, 239, 252)
        self.font = pygame.font.SysFont('freesansbold.ttf', fontSize)

    def draw(self, surface, text, xdim, ydim, x_top_left, y_top_left):
        rect_obj = pygame.draw.rect(surface, self.light_blue, pygame.Rect(
            x_top_left, y_top_left, xdim, ydim))
        text_surface_object = self.font.render(text, True, self.light_purple)
        text_rect = text_surface_object.get_rect(
            center=rect_obj.center)
        surface.blit(text_surface_object, text_rect)

    def addText(self, surface, text, xdim, ydim, x_top_left, y_top_left):
        size_x, size_y = self.font.size(text)
        if size_x > xdim:
            s1 = text[:len(text)//2]
            s2 = text[len(text)//2:]
            self.draw(surface, s1, xdim, ydim /
                      2, x_top_left, y_top_left)
            self.draw(surface, s2, xdim, ydim/2,
                      x_top_left, y_top_left+ydim/2)
        else:
            self.draw(surface, text, xdim, ydim,
                      x_top_left, y_top_left)
