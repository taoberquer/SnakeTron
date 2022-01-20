import pygame

from food import Food
from score import Score
from snake import Snake


class Round:
    def __init__(self, screen, settings):
        self.screen = screen
        self.snakes = [Snake(100, 200, settings), Snake(400, 200, settings)]
        self.score = Score()
        self.game_over = False
        self.food = self.generate_food()

    def run(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.display_snakes()
            self.screen.blit(self.food.image, self.food.rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    self.user_input(event.key)

            self.snakes_move()
            pygame.time.Clock().tick(5)

    def user_input(self, key):
        switch = {
            pygame.K_UP: 'up',
            pygame.K_DOWN: 'down',
            pygame.K_LEFT: 'left',
            pygame.K_RIGHT: 'right'
        }
        if key in switch:
            self.snakes[0].set_direction(switch[key])
        if not self.settings['multiplayer']:
            return
        switch = {
            pygame.K_z: 'up',
            pygame.K_s: 'down',
            pygame.K_q: 'left',
            pygame.K_d: 'right'
        }
        if key in switch:
            self.snakes[1].set_direction(switch[key])

    def generate_food(self):
        return Food()

    def display_snakes(self):
        for snake in self.snakes:
            for part in snake.body:
                self.screen.blit(part.image, part.rect)

    def snakes_move(self):
        for snake in self.snakes:
            snake.move()
        if self.snakes_collide(self.snakes):
            self.game_over = True
            return
        for snake in self.snakes:
            snake.remove_last_body()
        if self.snakes_check_food_collision(self.food):
            self.food = self.generate_food()

    def snakes_collide(self, snakes):
        for snake in snakes:
            for other_snake in snakes:
                if snake != other_snake:
                    if snake.check_collision(other_snake):
                        return True

    def snakes_check_food_collision(self, food):
        for snake in self.snakes:
            if snake.check_food_collision(food):
                return True