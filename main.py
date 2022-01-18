import pygame

from game import Game

pygame.init()

screen = pygame.display.set_mode((800, 600))

game = Game(screen)

# start game loop
while not game.game_over:

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = game.game_over = True
        elif event.type == pygame.KEYDOWN:
            game.user_input(event.key)
    game.move_snake()
    screen.fill((0, 0, 0))
    screen.blit(game.snake.image, game.snake.rect)

    pygame.display.flip()
    pygame.time.Clock().tick(10)
