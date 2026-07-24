import pygame
from math import cos, sin, tau
from settings import *

class Player:
    def __init__(self, game, engine):
        self.game = game
        self.engine = engine
        self.PLAYER_SPD = 0.001
        self.PLAYER_ROTATE_SPD = 0.001
        self.PLAYER_A = 0
        self.X, self.Y = 2.5,1.5
        self.body = 0.5
        self.playerHp = 100
        self.shot = False

    @property
    def player_pos_map(self):
        return (int(self.X), int(self.Y))

    @property
    def player_pos(self):
        return (self.X, self.Y)

    def key_board(self):
        cos_a = cos(self.PLAYER_A)
        sin_a = sin(self.PLAYER_A)
        speed = self.PLAYER_SPD * self.engine.del_time
        cos_spd = speed * cos_a
        sin_spd = speed * sin_a

        dx, dy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += cos_spd
            dy += sin_spd
        if keys[pygame.K_s]:
            dx -= cos_spd
            dy -= sin_spd
        if keys[pygame.K_d]:
            dy += cos_spd
            dx -= sin_spd
        if keys[pygame.K_a]:
            dy -= cos_spd
            dx += sin_spd

        # if keys[pygame.K_o]:
        #     self.PLAYER_A += self.PLAYER_ROTATE_SPD * self.engine.del_time
        # if keys[pygame.K_p]:
        #     self.PLAYER_A -= self.PLAYER_ROTATE_SPD * self.engine.del_time
        
        self.try_move(dx, dy)

    def commandShot(self, event):
        cmdShot = pygame.mouse.get_pressed()
        if not self.shot and cmdShot[0] and not self.game.curr_wpn.reload:
            #debug
            # print("shoot")
            self.shot = True

    def changeWeapons(self, event):
        if event.key == pygame.K_1:
            self.game.curr_wpn = self.game.wpns['1']
            #for debug
            # print("key pressed")
        if event.key == pygame.K_2:
            self.game.curr_wpn = self.game.wpns['2']
            #for debug
            # print("key pressed") 

    def mouse_movement(self):
        self.mouse_x = pygame.mouse.get_rel()[0]
        self.mouse = self.mouse_x * SENSITIVITY * self.engine.del_time
        self.PLAYER_A += self.mouse
        self.PLAYER_A %= tau

    def try_move(self, dx, dy):
        scale = 10
        if self.check_wall(self.X+dx*scale, self.Y):
            self.X += dx
        if self.check_wall(self.X, self.Y+dy*scale):
            self.Y += dy

    def check_wall(self, x, y):
        return (int(x), int(y)) not in self.game.map.walls


    def update(self):
        self.key_board()
        self.mouse_movement()

    def draw(self):
        pygame.draw.circle(self.engine.window,(255,0,0),(self.X*100,self.Y*100), 15)