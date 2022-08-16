from ctypes import alignment
from turtle import left
import pygame

# title text class


class WrapTextDisplay():
    def __init__(self, text_input, fontSize, x, y):
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 128)
        self.x_pos = x
        self.y_pos = y
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.white)
        self.textRect = self.text.get_rect(
            topleft=(self.x_pos, self.y_pos))

    def setText(self, newText):
        self.text_input = newText
        self.text = self.font.render(newText, True, self.white)
        self.textRect = self.text.get_rect(topleft=(self.x_pos, self.y_pos))

    def draw(self, surface):
        surface.blit(self.text, self.textRect)

    def addText(self, surface, newText, xdim, ydim, x_top_left, y_top_left):
        size_x, size_y = self.font.size(newText)
        if size_x > xdim:
            s1 = newText[:len(newText)//2]
            s2 = newText[len(newText)//2:]
            self.addCenteredText(surface, s1, xdim, ydim /
                                 2, x_top_left, y_top_left)
            self.addCenteredText(surface, s2, xdim, ydim/2,
                                 x_top_left, y_top_left+ydim/2)
        else:
            self.addCenteredText(surface, text, xdim, ydim,
                                 x_top_left, y_top_left)
