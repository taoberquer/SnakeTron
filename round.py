import pygame
import random

from food import Food
from wormhole import Wormhole
from score import Score
from snake import Snake

class Round:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.snakes = self.init_sakes()
        self.score = Score()
        self.game_over = False
        self.specials = {}
        self.generate_food()
        self.wormhole = None
        self.specials['wormhole_first'] = None
        self.specials['wormhole_sec'] = None
        self.font = pygame.font.Font(None, 24)
        self.font_color = (255,255,255)
        self.font_background = (0,0,0)

    def init_sakes(self):
        snakes = [Snake(100, 200, self.settings)]
        if self.settings['multiplayer']:
            snakes.append(Snake(400, 200, self.settings))
        return snakes

    def run(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            if self.settings['wormhole']:
                self.generate_worm_whole()
            self.display_snakes()
            self.update_ath()
            self.display_specials()

            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    self.user_input(event.key)

            self.snakes_move()
            pygame.time.Clock().tick(15)
        
        self.save_best_score()
    
    def update_ath(self):
        # Player1 score
        player1_score = self.font.render(f"Score : {len(self.snakes[0].body) - 1}", True, self.font_color, self.font_background)
        player1_score_rect = player1_score.get_rect()
        player1_score_rect.x, player1_score_rect.y = 10, 10
        self.screen.blit(player1_score, player1_score_rect)

        # Player2 score
        if self.settings['multiplayer']:
            player2_score = self.font.render(f"Score : {len(self.snakes[1].body) - 1}", True, self.font_color, self.font_background)
            player2_score_rect = player2_score.get_rect()
            player2_score_rect.topright = (self.settings['screen_width'] - 10, 10)
            self.screen.blit(player2_score, player2_score_rect)

        # best score 
        best_score = self.font.render(f"Best score : {self.score.best_score}", True, self.font_color, self.font_background)   
        best_score_rect = best_score.get_rect()
        best_score_rect.centerx = self.settings['screen_width'] / 2
        best_score_rect.y = 10
        self.screen.blit(best_score, best_score_rect)

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
        self.specials["food"] = Food(self.specials, self.settings['size'])

    def generate_worm_whole(self):        
        num = random.randint(0, 100)
        if num == 1:
            self.wormhole = None
            self.specials['wormhole_first'] = None
            self.specials['wormhole_sec'] = None
            self.wormhole = Wormhole(self.specials, self.settings['size'])
            self.specials['wormhole_first'] = self.wormhole.first
            self.specials['wormhole_sec'] = self.wormhole.sec

    def display_snakes(self):
        for snake in self.snakes:
            for part in snake.body:
                self.screen.blit(part.image, part.rect)

    def snakes_move(self):
        for snake in self.snakes:
            snake.move(self.specials)
        if self.snakes_collide(self.snakes):
            self.game_over = True
            return
        if self.snakes_check_food_collision(self.specials['food']):
            self.generate_food()

    def snakes_collide(self, snakes):
        if not self.settings['multiplayer']:
            return snakes[0].check_collision(None)
        
        for snake in snakes:
            for other_snake in snakes:
                if snake != other_snake:
                    if snake.check_collision(other_snake):
                        return True

    def snakes_check_food_collision(self, food):
        for snake in self.snakes:
            if snake.check_food_collision(food):
                return True
    
    def save_best_score(self):
        best_score = max([len(snake.body) for snake in self.snakes])
        if self.score.best_score < best_score:
            self.score.save_score(best_score - 1)

    def display_specials(self):
        self.screen.blit(self.specials['food'].image, self.specials['food'].rect)

        if self.specials['wormhole_first']:
            self.screen.blit(self.specials['wormhole_first'].image, self.specials['wormhole_first'].rect)
            self.screen.blit(self.specials['wormhole_sec'].image, self.specials['wormhole_sec'].rect)
