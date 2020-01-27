import pygame
from random import *

class Pipe(pygame.sprite.Sprite):

    def __init__(self, velocity, random_x_position, random_y_position, surface):
        super().__init__()
        self.surface = surface
        self.random_y_position = random_y_position
        self.random_x_position = random_x_position
        self.image = pygame.image.load('assets/pipe.png')
        self.image = pygame.transform.scale(self.image, (40, 240))
        self.velocity = velocity
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.rect.y = self.random_y_position
        self.rect.x = self.surface.get_width() + self.random_x_position

    def move(self):
        self.rect.x -= self.velocity