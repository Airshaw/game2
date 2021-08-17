import pygame
import pytmx
import pyscroll
import animation

from player import Player


class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("nouveau jeux")
        tmx_data = pytmx.util_pygame.load_pygame("carte1.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_data.visible_object_layers()
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        self.fps = 60

        self.player = Player(527.33, 154.00, tmx_data)
        self.walls = []
        for obj in tmx_data.objects:
            print(obj.type)
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.groupe = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.groupe.add(self.player)

        enter_house = tmx_data.get_object_by_name('enter_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    def switch_house(self):
        tmx_data = pytmx.util_pygame.load_pygame("house.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_data.visible_object_layers()
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        self.fps = 60
        self.walls = []
        for obj in tmx_data.objects:
            print(obj.type)
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.groupe = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.groupe.add(self.player)

        enter_house = tmx_data.get_object_by_name('exit_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)
        spawn_house_point = tmx_data.get_object_by_name('enter_house_exit')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20

    def switch_world(self):
        tmx_data = pytmx.util_pygame.load_pygame("carte1.tmx.")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_data.visible_object_layers()
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        self.fps = 60
        self.walls = []
        for obj in tmx_data.objects:
            print(obj.type)
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.groupe = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.groupe.add(self.player)

        enter_house = tmx_data.get_object_by_name('enter_exit')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        spawn_house_point = tmx_data.get_object_by_name('enter_house_exit')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y + 20

    def update(self):
        self.groupe.update()

        if self.player.feet.colliderect(self.enter_house_rect):
            self.switch

        for sprite in self.groupe.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                self.player.move_back()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:

            self.player.save_location()
            self.update()
            self.groupe.center(self.player.rect)
            self.groupe.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        self.clock.tick(self.fps)
        pygame.quit(

        )