import pygame

from game import Game

pygame.init()

settings = {
    'screen_width': 800,
    'screen_height': 600,
    'size': 20,
}

screen = pygame.display.set_mode((settings['screen_width'], settings['screen_height']))

game = Game(screen, settings)

game.run()
