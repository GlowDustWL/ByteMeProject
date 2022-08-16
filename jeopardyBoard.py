# import statements
import pygame
import textDisplayBoardWrap


class JeopardyBoard:

    def __init__(self):
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

        # Dollar amount boxes
        self.dollar = ['$200', '$400', '$600', '$800', '$1000']

        # initialize matrix to determine which squares to show. "True" means "show", "False" means "don't show"
        self.showMatrix = [[[] for i in range(5)] for j in range(6)]
        for x in range(6):
            for y in range(5):
                self.showMatrix[x][y] = True

    def draw(self, surface, categories):

        # get mouse position
        pos = pygame.mouse.get_pos()

        # Draw title boxes
        pygame.draw.rect(surface, self.dark_blue, pygame.Rect(
            self.title_x_start, self.title_y_start, self.title_x_dim, self.title_y_dim))
        for x in range(6):
            thisBox = textDisplayBoardWrap.Pane(32)
            thisBox.addText(surface, categories[x], self.x_dim, self.y_dim, self.title_x_start+self.x_pad +
                            self.x_dim*x+self.x_pad*x, self.title_y_start+self.y_pad)
        # Draw sub boxes
        pygame.draw.rect(surface, self.dark_blue, pygame.Rect(
            self.full_x_start, self.full_y_start, self.full_x_dim, self.full_y_dim-self.y_dim-self.y_pad*2))
        for x in range(6):
            for y in range(5):
                if self.showMatrix[x][y]:
                    rect_obj = pygame.draw.rect(surface, self.light_blue, pygame.Rect(self.title_x_start+self.x_pad+self.x_dim*x+self.x_pad*x,
                                                                                      self.title_y_start+self.y_pad+self.y_dim*y+self.y_pad*y+self.y_dim+3*self.y_pad, self.x_dim, self.y_dim))
                    text_surface_object = pygame.font.SysFont(
                        'freesansbold.ttf', 32).render(self.dollar[y], True, self.light_purple)
                    text_rect = text_surface_object.get_rect(
                        center=rect_obj.center)
                    surface.blit(text_surface_object, text_rect)

    def removeSquare(self, surface, x, y):
        # rect_obj = pygame.draw.rect(surface, self.light_blue, pygame.Rect(self.title_x_start+self.x_pad+self.x_dim*x+self.x_pad*x,
        #                                                                   self.title_y_start+self.y_pad+self.y_dim*y+self.y_pad*y+self.y_dim+3*self.y_pad, self.x_dim, self.y_dim))
        self.showMatrix[x][y] = False

    def highlightSquare(self, surface, x, y):
        rect_obj = pygame.draw.rect(surface, self.light_purple, pygame.Rect(self.title_x_start+self.x_pad+self.x_dim*x+self.x_pad*x,
                                                                            self.title_y_start+self.y_pad+self.y_dim*y+self.y_pad*y+self.y_dim+3*self.y_pad, self.x_dim, self.y_dim))
        text_surface_object = pygame.font.SysFont(
            'freesansbold.ttf', 32).render(self.dollar[y], True, self.light_blue)
        text_rect = text_surface_object.get_rect(
            center=rect_obj.center)
        surface.blit(text_surface_object, text_rect)
