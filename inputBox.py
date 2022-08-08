import pygame

# inputBox class


class InputBox():
    def __init__(self, text_input, font_size, x, y):
        print("in init")
        self.font = pygame.font.Font('freesansbold.ttf', font_size)
        self.active_color = (0, 0, 128)
        self.passive_color = (0, 0, 50)
        self.x_pos = x
        self.y_pos = y
        self.text_input = text_input
        self.input_rect = pygame.Rect(self.x_pos, self.y_pos, 140, 32)
        self.current_color = self.passive_color
        self.text = self.font.render(self.text_input, True, (255, 255, 255))
        self.clicked = False

    def draw(self, surface, text_input):
        pygame.draw.rect(surface, self.current_color, self.input_rect)
        text_surface = self.font.render(
            text_input, True, (255, 255, 255))
        surface.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        self.input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()

    def clear(self):
        self.text_input = ""
