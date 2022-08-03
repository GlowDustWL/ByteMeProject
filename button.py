import pygame

# button class


class Button():
    def __init__(self, text_input, font_size, x, y):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        white = (255, 255, 255)
        blue = (0, 0, 128)
        self.x_pos = x
        self.y_pos = y
        self.text_input = text_input
        self.text = font.render(self.text_input, True, white)
        self.text_hover = font.render(self.text_input, True, blue)
        self.textRect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        self.clicked = False

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.textRect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            surface.blit(self.text_hover, self.textRect)
        else:
            surface.blit(self.text, self.textRect)
