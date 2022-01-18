import pygame


class Food:
    def __init__(self):
        self.image = pygame.Surface((20, 20))
        self.image.fill((202, 0, 42))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100