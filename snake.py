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
        vertical = ["up", "down"]
        horizontal = ["left", "right"]
        if direction in vertical and self.direction in vertical:
            return
        if direction in horizontal and self.direction in horizontal:
            return
        self.direction = direction

    def move(self, specials):
        if self.direction == "right":
            self.rect.x += self.vel
            if self.settings["toric_grid"] and self.rect.x > self.settings['screen_width']:
                self.rect.x = 0

        elif self.direction == "left":
            self.rect.x -= self.vel
            if self.settings["toric_grid"] and self.rect.x < 0:
                self.rect.x = self.settings['screen_width'] - self.settings['size']

        elif self.direction == "up":
            self.rect.y -= self.vel
            if self.settings["toric_grid"] and self.rect.y < 0:
                self.rect.y = self.settings['screen_height'] - self.settings['size']

        elif self.direction == "down":
            self.rect.y += self.vel
            if self.settings["toric_grid"] and self.rect.y > self.settings['screen_height']:
                self.rect.y = 0
            
        if self.settings["wormhole"] and specials['wormhole_first']:
                self.cross_wormhole(specials)

        self.remove_last_body()
        self.generate_body()

    def check_collision(self, other_snake):
        if self.check_self_collision():
            return True

        if not self.settings['toric_grid'] and self.check_walls_collision():
            return True
        
        if self.check_snake_collision(other_snake):
            return True
                
        return False


    def check_walls_collision(self):   
        return self.rect.x < 0 or self.rect.x > self.settings['screen_width']-self.settings['size'] or self.rect.y < 0 or self.rect.y > \
                self.settings['screen_height']-self.settings['size']    

    def check_self_collision(self):
        for index, body in enumerate(self.body):
            if (index != len(self.body) - 1) and (self.rect.x == body.rect.x and self.rect.y == body.rect.y):
                return True
        return False

    def check_snake_collision(self, other_snake):
        if other_snake:
            for index, body in enumerate(other_snake.body):
                if self.rect.x == body.rect.x and self.rect.y == body.rect.y:
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
    
    def cross_wormhole(self, specials):

        if (self.rect.x == specials['wormhole_first'].rect.x and self.rect.y == specials['wormhole_first'].rect.y):
            if self.direction == "right":
                self.rect.x = specials['wormhole_sec'].rect.x + self.settings['size']
                self.rect.y = specials['wormhole_sec'].rect.y
            elif self.direction == "left":
                self.rect.x = specials['wormhole_sec'].rect.x - self.settings['size']
                self.rect.y = specials['wormhole_sec'].rect.y
            elif self.direction == "up":
                self.rect.x = specials['wormhole_sec'].rect.x 
                self.rect.y = specials['wormhole_sec'].rect.y - self.settings['size']
            elif self.direction == "down":
                self.rect.x = specials['wormhole_sec'].rect.x 
                self.rect.y = specials['wormhole_sec'].rect.y + self.settings['size']
        
        if (self.rect.x == specials['wormhole_sec'].rect.x and self.rect.y == specials['wormhole_sec'].rect.y):
            if self.direction == "right":
                self.rect.x = specials['wormhole_first'].rect.x + self.settings['size']
                self.rect.y = specials['wormhole_first'].rect.y
            elif self.direction == "left":
                self.rect.x = specials['wormhole_first'].rect.x - self.settings['size']
                self.rect.y = specials['wormhole_first'].rect.y
            elif self.direction == "up":
                self.rect.x = specials['wormhole_first'].rect.x 
                self.rect.y = specials['wormhole_first'].rect.y - self.settings['size']
            elif self.direction == "down":
                self.rect.x = specials['wormhole_first'].rect.x 
                self.rect.y = specials['wormhole_first'].rect.y + self.settings['size']