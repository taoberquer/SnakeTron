import pygame

from body import Body


class Snake:
    def __init__(self, x, y, settings):
        self.image = pygame.Surface((settings['size'], settings['size']))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = settings['size']
        self.body = []
        self.length = 1
        self.direction = "right"
        self.settings = settings
        self.generate_body()

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
        self.generate_body()

    def check_collision(self, other_snake):
        if self.rect.x < 0 or self.rect.x > self.settings['screen_width'] or self.rect.y < 0 or self.rect.y > \
                self.settings['screen_height']:
            return True
        for index, body in enumerate(other_snake.body):
            if self.rect.x == body.rect.x and self.rect.y == body.rect.y:
                return True
        for index, body in enumerate(self.body):
            if (index != len(self.body) - 1) and (self.rect.x == body.rect.x and self.rect.y == body.rect.y):
                return True
        return False


    def check_food_collision(self, food):
        if self.rect.x == food.rect.x and self.rect.y == food.rect.y:
            self.eat_food()
            return True
        return False

    def generate_body(self):
        self.body.append(Body(self.rect.x, self.rect.y, self.settings['size']))

    def eat_food(self):
        self.length += 1
        self.body.insert(0, Body(self.body[0].rect.x, self.body[0].rect.y, self.settings['size']))

    def remove_last_body(self):
        self.body.pop(0)