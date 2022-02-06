import random

import pygame


class Special:
    def __init__(self, specials, color, size, random=True, x=0, y=0):
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.specials = specials
        self.size = size
        self.random = random
        self.generate_position()

    def generate_position(self):
        if self.random:
            self.rect.x = random.randint(0, 800) // self.size * self.size
            self.rect.y = random.randint(0, 600) // self.size * self.size
            if not self.check_free_position():
                self.generate_position()
    
    def check_free_position(self):
        print(self.specials)
        for special in self.specials:
            if self.specials[special]:
                if isinstance(self.specials[special], list):
                    for special_list in self.specials[special]:
                        if special_list.rect.x == self.rect.x and special_list.rect.y == self.rect.y:
                            return False
                elif self.specials[special].rect.x == self.rect.x and self.specials[special].rect.y == self.rect.y:
                    return False
        return True