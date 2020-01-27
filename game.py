import pygame
from pipegroup import PipeGroup
from bird import Bird

class Game:

    def __init__(self, screen):
        self.score = 0
        self.playing = True
        self.screen = screen
        self.pipegr1 = PipeGroup(self, screen, 10)
        self.pipegr2 = PipeGroup(self, screen, self.pipegr1.get_x())
        self.pipegr3 = PipeGroup(self, screen, self.pipegr2.get_x())
        self.pipegroups = [self.pipegr1, self.pipegr2, self.pipegr3]
        self.bird = Bird(self, screen, self.pipegroups)

    def update(self, base, x_base):
        for pipegroup in self.pipegroups:
            # deplacement des tuiles
            pipegroup.move()

            # dessiner toutes les tuiles
            pipegroup.group.draw(self.screen)

        # appliquer la base
        self.screen.blit(base, (x_base, 400))

        # faire l'animation de chut de notre oiseau
        self.bird.update()

        # appliquer l'oiseau
        self.screen.blit(self.bird.image, self.bird.rect)

        # appliquer score
        self.update_score()


    def update_score(self):
        score_text = pygame.font.SysFont("monospace", 24).render("{0}".format(self.score), 1, (0, 0, 0))
        self.screen.blit(score_text, (12, 12))

    def reset(self):
        self.score = 0
        self.playing = False
        self.bird.respawn()
        
        for pipegroup in self.pipegroups:
            pipegroup.respawn()