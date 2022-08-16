import pygame
from pygame.locals import *


class Pane:
    def __init__(self, text_input, fontSize, xdim, ydim, x_top_left, y_top_left):
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont('freesansbold.ttf', fontSize)
        self.xdim = xdim
        self.ydim = ydim
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.text_input = text_input
        self.text_surface_object = self.font.render(
            self.text_input, True, self.white)
        self.text_rect = self.text_surface_object.get_rect(
            center=(self.x_top_left, self.y_top_left))

    def setText(self, text, y_top_left):
        self.text_surface_object = self.font.render(text, True, self.white)
        self.text_rect = self.text_surface_object.get_rect(
            center=(self.x_top_left, y_top_left))

    def addText(self, text):
        size_x, size_y = self.font.size(text)
        if size_x > self.xdim:
            s1 = text[:len(text)//2]
            s2 = text[len(text)//2:]
            print(s1)
            print(s2)
            self.setText(s1, self.y_top_left)
            self.setText(s2, self.y_top_left+self.ydim/2)
        else:
            self.setText(text, self.y_top_left)

    def draw(self, surface):
        surface.blit(self.text_surface_object, self.text_rect)
