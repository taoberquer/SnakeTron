import pygame


class Snake:
    def __init__(self, settings):
        self.image = pygame.Surface((settings['size'], settings['size']))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 0
        self.vel = settings['size']
        self.body = []
        self.length = 1
        self.direction = "right"
        self.settings = settings

    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == "right":
            self.rect.x += self.vel
        elif self.direction == "left":
            self.rect.x -= self.vel
        elif self.direction == "up":
            self.rect.y -= self.vel
        elif self.direction == "down":
            self.rect.y += self.vel

    def check_collision(self):
        if self.rect.x < 0 or self.rect.x > self.settings['screen_width'] or self.rect.y < 0 or self.rect.y > self.settings['screen_height']:
            return True
        for body in self.body:
            if self.rect.x == body.rect.x and self.rect.y == body.rect.y:
                return True
        return False

    def check_food_collision(self, food):
        if self.rect.x == food.rect.x and self.rect.y == food.rect.y:
            return True
        return False

    def eat_food(self):
        self.length += 1
