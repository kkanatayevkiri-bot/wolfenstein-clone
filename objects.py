import pygame
import os
from settings import *
from math import atan2, hypot, pi, tau, cos

class Objects:
    def __init__(self, game, path="/textures/objects/candlebra.png", pos=(6.5,1.5), offset=0.27, scale=0.5):
        self.game = game
        self.offset = offset
        self.scale = scale
        self.basePath = os.path.dirname(os.path.abspath(__file__))
        self.image = pygame.image.load(self.basePath+path).convert_alpha()
        self.w, self.h = self.image.get_width(), self.image.get_height()
        self.half_w = self.w / 2
        self.ratio = self.w / self.h
        self.x , self.y = pos

    def render(self):
        px, py  = self.game.player.player_pos
        dx ,dy = self.x - px , self.y - py
        theta = atan2(dy ,dx)
        delta = theta - self.game.player.PLAYER_A
        if (dx > 0 and self.game.player.PLAYER_A > pi) or (dx < 0 and dy < 0):
            delta += tau

        del_rays = delta / DEL_RAY
        self.dist = hypot(dx, dy)
        self.dist *= cos(delta)
        self.x_screen = (HALF_NUM_RAYS + del_rays) * SCALE
        if -self.half_w < self.x_screen < (X+self.half_w):
            self.show()

    def show(self):
        obj_h = DISTANCE / self.dist * self.scale
        obj_w = obj_h * self.ratio
        img = pygame.transform.scale(self.image,(obj_w,obj_h))
        height_shift = obj_h * self.offset
        pos = self.x_screen - obj_w // 2, HALF_Y - obj_h // 2 + height_shift
        self.game.rays.wall_results.append((img, pos, self.dist))

    def update(self):
        self.render()
