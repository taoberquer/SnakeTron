import pygame_menu

from round import Round


class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        print(self.settings)


    def start_the_game(self):
        print(self.settings)
        round = Round(self.screen, self.settings)
        round.run()
        pygame_menu.events.EXIT



    def launch(self):
        menu = pygame_menu.Menu('El Sneko del fuego', self.settings['screen_width'], self.settings['screen_height'], theme=pygame_menu.themes.THEME_DARK)
        menu.add.selector('Multijoueur : ', [('NON', False), ('OUI', True)], onchange=self.multiplayer)
        menu.add.selector('Grille torique : ', [('NON', False), ('OUI', True)], onchange=self.toric_grid)
        menu.add.selector('Trou de ver : ', [('NON', False), ('OUI', True)], onchange=self.wormhole)
        menu.add.selector('Murs aléatoires : ', [('NON', False), ('OUI', True)], onchange=self.random_walls)
        menu.add.selector('Murs aléatoires dynamiques : ', [('NON', False), ('OUI', True)], onchange=self.dynamic_random_walls)
        menu.add.selector('Réduction : ', [('NON', False), ('OUI', True)], onchange=self.reduction)

        menu.add.button('Jouer', self.start_the_game)
        menu.add.button('Quitter', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def multiplayer(self, *args):
        self.settings['multiplayer'] = args[1]

    def toric_grid(self, *args):
        self.settings['toric_grid'] = args[1]

    def wormhole(self, *args):
        self.settings['wormhole'] = args[1]

    def random_walls(self, *args):
        self.settings['random_walls'] = args[1]

    def dynamic_random_walls(self, *args):
        self.settings['dynamic_random_walls'] = args[1]

    def reduction(self, *args):
        self.settings['reduction'] = args[1]