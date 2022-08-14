# import pygame

# # button class


# class ButtonJeopardyBoard():
#     def __init__(self,x, y, clickable=True):
#         white = (255, 255, 255)
#         blue = (0, 0, 128)
#         # grey = (115, 115, 115)
#         self.x_pos = x
#         self.y_pos = y
#         self.text_hover = font.render(self.text_input, True, blue)
#         self.text_unclickable = font.render(self.text_input, True, white)
#         self.text_unclickable.set_alpha(90)
#         self.textRect = self.text.get_rect(center=(self.x_pos, self.y_pos))
#         self.clickable = clickable

#         self.clicked = False

#     def draw(self, surface):
#         action = False

#         pos = pygame.mouse.get_pos()

#         if self.clickable:
#             if self.textRect.collidepoint(pos):
#                 if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#                     self.clicked = True
#                     action = True

#                 if pygame.mouse.get_pressed()[0] == 0:
#                     self.clicked = False

#                 surface.blit(self.text_hover, self.textRect)
#             else:
#                 surface.blit(self.text, self.textRect)
#         else:
#             surface.blit(self.text_unclickable, self.textRect)
#             self.clicked = False

#     def setClickable(self, clickableInput):
#         if clickableInput:
#             self.clickable = True
#         elif clickableInput == False:
#             self.clickable = False