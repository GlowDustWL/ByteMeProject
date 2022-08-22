import pygame

# button class


class ButtonJeopardyBoard():
    def __init__(self, x, y):
        # store indices
        self.x = x
        self.y = y

        # initalize colors
        self.dark_blue = (38, 54, 150)
        self.light_purple = (190, 25, 207)
        self.light_blue = (83, 239, 252)
        self.color = (255, 0, 0)
        self.color2 = (0, 255, 0)
        self.white = (255, 255, 255)

        # full board size
        self.full_x_dim = 600
        self.full_y_dim = 480

        # board padding
        self.x_pad = 10
        self.y_pad = 10

        # board box sizes
        self.x_dim = (self.full_x_dim - self.x_pad*8)/6
        self.y_dim = (self.full_y_dim - self.y_pad*8)/6

        # title alignment
        self.title_x_start = 950
        self.title_y_start = 50
        self.title_y_dim = self.y_dim + self.y_pad*2

        # board alignment
        self.full_x_start = self.title_x_start
        self.full_y_start = self.title_y_start + self.title_y_dim + 10
        self.title_x_dim = self.full_x_dim

        # button rect
        self.buttonRect = pygame.Rect(self.title_x_start+self.x_pad+self.x_dim*self.x+self.x_pad*self.x,
                                      self.title_y_start+self.y_pad+self.y_dim*self.y+self.y_pad*self.y, self.x_dim, self.full_y_dim-self.y_pad)

        self.clickable = True

        self.clicked = False

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.clickable:
            if self.buttonRect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                rect_obj = pygame.draw.rect(
                    surface, self.light_purple, self.buttonRect, 6)
            else:
                rect_obj = pygame.draw.rect(
                    surface, self.white, self.buttonRect, 6)
                self.clicked = False
        else:
            self.clicked = False

    # def setClickable(self, clickableInput):
    #     if clickableInput:
    #         self.clickable = True
    #     elif clickableInput == False:
    #         self.clickable = False
