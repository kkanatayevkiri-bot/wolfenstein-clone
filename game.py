import pygame
from map import *
from player import *
from raycast import *
from objectrenderer import *
from objectHandler import *
from weapons import *
from dfs import *

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
        self.path = FindPath(self)
        self.object_handeler = ObjectHandeler(self)
        self.wpns = {'1':Weapons(self), '2':MachineGun(self)}
        self.curr_wpn = self.wpns['2']

    def input(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.done = True
            self.player.changeWeapons(event)
        self.player.commandShot(event)

    def update(self):
        self.player.update()
        self.rays.update()
        self.object_handeler.update()
        self.curr_wpn.update()

    def draw(self):
        self.engine.window.fill((0,0,0))
        self.object_renderer.draw()
        self.curr_wpn.draw(self.engine.window)