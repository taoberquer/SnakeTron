import random

import pygame

from food import Food
from snake import Snake


class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.snake = Snake(settings)
        self.score = 0
        self.game_over = False
        self.food = self.generate_food()

    def run(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.snake.image, self.snake.rect)
            self.screen.blit(self.food.image, self.food.rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    self.user_input(event.key)

            self.move_snake()
            pygame.time.Clock().tick(5)

    def user_input(self, key):
        switch = {
            pygame.K_UP: 'up',
            pygame.K_DOWN: 'down',
            pygame.K_LEFT: 'left',
            pygame.K_RIGHT: 'right'
        }
        if key in switch:
            self.snake.set_direction(switch[key])

    def move_snake(self):
        self.snake.move()
        if self.snake.check_collision():
            self.game_over = True
            return
        if self.snake.check_food_collision(self.food):
            self.score += 1
            self.snake.eat_food()
            self.food = self.generate_food()

    def generate_food(self):
        return Food()
