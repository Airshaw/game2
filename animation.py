import pygame


# definir une classe
class AnimateSprite(pygame.sprite.Sprite):

    # definir  la creation de l'entité

    def __init__(self, player):
        super(AnimateSprite, self).__init__()
        self.image = pygame.image.load('player.png')
