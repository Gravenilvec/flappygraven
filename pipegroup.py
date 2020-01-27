import pygame
from pipe import Pipe
from random import *

class PipeGroup():

    def __init__(self, game, surface, last_pipegroup_x):
        self.surface = surface
        self.game = game
        self.last_pipegroup_x = last_pipegroup_x
        self.distance = 120
        self.velocity = 1
        self.group = pygame.sprite.Group() 
        self.random_x_position = self.last_pipegroup_x + randint(100, 300)
        self.random_y_position = randint(180, 300)

        # tuile bas
        self.pipe_bottom = Pipe(self.velocity, self.random_x_position, self.random_y_position, self.surface)
        self.group.add(self.pipe_bottom)

        # tuile haut
        self.pipe_top = Pipe(self.velocity, self.random_x_position, self.random_y_position, self.surface)
        self.pipe_top.rect.y = self.pipe_bottom.rect.y - (self.pipe_top.height + self.distance)
        self.pipe_top.image = pygame.transform.rotate(self.pipe_top.image, 180)
        self.group.add(self.pipe_top)

    def move(self):
        self.pipe_top.move()
        self.pipe_bottom.move()

        # si on est au meme endroit que le oiseau
        if self.pipe_top.rect.x == self.game.bird.rect.x:
            self.game.score += 1

        # si sort de l'ecran
        if self.pipe_top.rect.x + self.pipe_bottom.rect.width < 0:
            self.respawn()

    def respawn(self):
        self.random_x_position = self.last_pipegroup_x + randint(100, 300)
        self.random_y_position = randint(180, 300)

        self.pipe_bottom.rect.x = self.surface.get_width() + self.random_x_position
        self.pipe_bottom.rect.y = self.random_y_position
        
        self.pipe_top.rect.x = self.surface.get_width() + self.random_x_position
        self.pipe_top.rect.y = self.pipe_bottom.rect.y - (self.pipe_top.height + self.distance)

    def get_x(self):
        return self.pipe_top.rect.x
