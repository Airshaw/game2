import pygame


class Detect_touche:
    def __init__(self):
        self.position = []
        self.direction = ['down','left','right','up']
        self.tmp = "down"

    def handl_imput(self, position:list):

        pressed= pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            position[1] -= 1
            self.tmp=self.direction[3]

        if pressed[pygame.K_s]:
            position[1] += 1
            self.tmp = self.direction[0]

        if pressed[pygame.K_q]:
            position[0] -= 1
            self.tmp = self.direction[1]

        if pressed[pygame.K_d]:
            position[0] += 1
            self.tmp = self.direction[2]
        return (position,self.tmp)

    #ddcdcs