import pygame
import util

# title text class


class TextMedium():
    def __init__(self, text_input, x, y):
        self.font = pygame.font.Font(
            util.resourcePath('fonts/freesansbold.ttf'), 46)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 128)
        self.x_pos = x
        self.y_pos = y
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.white)
        self.textRect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def draw(self, surface):
        surface.blit(self.text, self.textRect)
