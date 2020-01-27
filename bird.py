import pygame


class Bird(pygame.sprite.Sprite):

    def __init__(self, game, surface, pipegroups):
        super().__init__()
        self.game = game
        self.pipegroups = pipegroups
        self.image = pygame.image.load('assets/bird.png')
        self.surface = surface
        self.rect = self.image.get_rect()
        self.vel_y = 0
        self.respawn()

    def fly(self):
        if self.rect.y - self.rect.height > 0:
            self.vel_y = -1.5

    def update(self):
        self.rect.y += self.vel_y
        self.vel_y += 0.04

        # si touche une tuile
        for pipegroup in self.pipegroups:
            if self.check_collision(pipegroup.group):
                self.game.reset()

        # si il tombe dans le vide, je le remet à 0
        if self.rect.y > self.surface.get_height():
            self.game.reset()

    def check_collision(self, pipegroup):
        return pygame.sprite.spritecollide(self, pipegroup, False, pygame.sprite.collide_mask)

    def respawn(self):
        self.vel_y = 0
        self.rect.x = int(self.surface.get_width()//3)
        self.rect.y = int(self.surface.get_height()//3)
