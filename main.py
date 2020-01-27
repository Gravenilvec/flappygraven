import pygame
from bird import Bird
from game import Game
pygame.init()

# creer la fenetre de notre jeu
screen = pygame.display.set_mode((285, 510))
pygame.display.set_caption("FlappyGravenGame")

# charger l'image de fond
background = pygame.image.load('assets/bg.jpg')

# charger l'image du fond explicatif (onboarding)
onboarding = pygame.image.load('assets/onboarding.png')

# charger la base qui va etre en déplacement
base = pygame.image.load('assets/base.png')

# valeur de x de ma base
x_base = 0
x_base_speed = 20

# variable pour stocker le jeu
game = Game(screen)

# boucle du jeu
while True:

    # ajouter / animer la valeur x_base
    x_base -= (x_base_speed/100)

    # si la valeur de x_base est inferieur à -100, on la remet à son point inital
    if x_base < -45: x_base = 0

    # appliquer l'image de l'arriere plan
    screen.blit(background, (0, 0))

    if game.playing:
        game.update(base, x_base)
    else:
        # appliquer le onboarding si le jeu n'est pas lancé
        screen.blit(onboarding, (screen.get_width()/2-onboarding.get_width()/2,
            screen.get_height()/2-onboarding.get_height()/2))

    pygame.display.flip()

    # recuperer les evenements actif du joueur
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.playing:
                game.bird.fly()
            else:
                game.playing = True
                print("redemarrage du jeu")