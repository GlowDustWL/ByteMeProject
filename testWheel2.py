import pygame

class Spinner(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load(
            'images/space_background.jpeg').convert()
        self.image = pygame.image.load(
            'images/space_background.jpeg').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.rotation_speed = 10
        self.last_animated = 0
        self.total_degrees_spun = 0
        self.spinning = False

    def update(self):
        if self.spinning:
            self.spin()

    def spin(self):
        now = pygame.time.get_ticks()
        if now - self.last_animated > 50:
            self.image = pygame.transform.rotate(self.original_image, -self.total_degrees_spun)
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.total_degrees_spun += self.rotation_speed
            self.rotation_speed -= .1
        if self.rotation_speed <= 0:
            self.spinning = False
            self.rotation_speed = 10

all_sprites = pygame.sprite.Group()
spinner = Spinner(100,100)
all_sprites.add(spinner)

all_sprites.update()