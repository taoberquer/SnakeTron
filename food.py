import random

import pygame


class Food:
    def __init__(self):
        self.image = pygame.Surface((20, 20))
        self.image.fill((202, 0, 42))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800) // 20 * 20
        self.rect.y = random.randint(0, 600) // 20 * 20