import random

import pygame
from snake import Snake


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.score = 0
        self.game_over = False
        self.food = self.generate_food()

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

    def generate_food(self):
        block_size = 20
        x = random.randint(0, 800 - block_size)
        y = random.randint(0, 600 - block_size)

        return pygame.Rect(x, y, block_size, block_size)
