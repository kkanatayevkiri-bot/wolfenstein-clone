import pygame
from map import *
from player import *
from raycast import *
from objectrenderer import *
from objects import *
from objectsAnimated import *
from weapons import *

class Game:
    def __init__(self,engine):
        self.engine = engine
        self.done = False
        self.next = "menu"
        self.curr = "game"
        self.new_game()

    def new_game(self):
        self.map = Map(self.engine)
        self.player = Player(self, self.engine)
        self.object_renderer = Objectrenderer(self)
        self.rays = Raycasting(self)
        self.object = Objects(self)
        self.aniObject = ObjectsAnimated(self)
        self.wp = Weapons(self)

    def input(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.done = True
        self.player.commandShot(event)

    def update(self):
        self.player.update()
        self.rays.update()
        self.object.update()
        self.aniObject.update()
        self.wp.update()

    def draw(self):
        self.engine.window.fill((0,0,0))
        self.object_renderer.draw()
        self.wp.draw(self.engine.window)
        # self.map.draw()
        # self.player.draw()