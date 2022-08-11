# import statements
import pygame
import os
clock = pygame.time.Clock()


class Wheel:

    def __init__(self):
        self.wheel_image = pygame.image.load(
            os.path.join('images', 'wheel_revA.png'))

        self.wheel_image = pygame.transform.smoothscale(
            self.wheel_image, (375, 375))

    def draw(self, surface):
        # get mouse position
        pos = pygame.mouse.get_pos()

        #surface.blit(self.wheel_image, (150, 60))
        surface.blit(self.wheel_image, (350 - int(self.wheel_image.get_width() / 2),
                                        250 - int(self.wheel_image.get_height() / 2)))

    def spin(self, surface, angle):
        mainClock = pygame.time.Clock()
        img = self.wheel_image

        # Loop ------------------------------------------------------- #
        for angle in range(0, angle, 2):
            img_copy = pygame.transform.rotate(img, angle)
            surface.blit(img_copy, (350 - int(img_copy.get_width() / 2),
                                    250 - int(img_copy.get_height() / 2)))
            # Update ------------------------------------------------- #
            pygame.display.update()
