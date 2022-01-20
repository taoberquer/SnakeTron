import pygame
import pygame_menu

from game import Game

pygame.init()

settings = {
    'screen_width': 800,
    'screen_height': 600,
    'size': 20,
    'user_number': 2,
    'toric_grid': False,
    'wormhole': False,
    'random_walls': False,
    'dynamic_random_walls': False,
    'reduction': False
}

screen = pygame.display.set_mode((settings['screen_width'], settings['screen_height']))

game = Game(screen, settings)

game.launch()