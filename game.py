import pygame_menu

from round import Round


class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings


    def start_the_game(self):
        round = Round(self.screen, self.settings)
        round.run()
        pygame_menu.events.EXIT



    def launch(self):
        menu = pygame_menu.Menu('El Sneko del fuego', self.settings['screen_width'], self.settings['screen_height'], theme=pygame_menu.themes.THEME_DARK)
        menu.add.selector('Nombre de joueurs : ', [('1', 1), ('2', 2)], onchange=self.set_user_number)
        menu.add.selector('Grille torique : ', [('OUI', True), ('NON', False), ('Difficile', 3)], onchange=self.toric_grid)
        menu.add.selector('Trou de ver : ', [('OUI', True), ('NON', False), ('Difficile', 3)], onchange=self.wormhole)
        menu.add.selector('Murs aléatoires : ', [('OUI', True), ('NON', False)], onchange=self.random_walls)
        menu.add.selector('Murs aléatoires dynamiques : ', [('OUI', True), ('2', False)], onchange=self.dynamic_random_walls)
        menu.add.selector('Réduction : ', [('OUI', True), ('NON', False)], onchange=self.reduction)

        menu.add.button('Jouer', self.start_the_game)
        menu.add.button('Quitter', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def set_user_number(self, *args):
        self.settings['user_number'] = args[1]

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