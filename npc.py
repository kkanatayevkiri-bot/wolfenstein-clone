import pygame
from objectsAnimated import *
from settings import *
from math import cos, sin, atan2

class Npc(ObjectsAnimated):
    def __init__(self,game , pos=(3.5,1.5) ,path='/textures/enemy/base/0.png' ,animation_time=120 , offset=0.27, scale=0.5):
        super().__init__(game, pos, path, animation_time, offset, scale)
        self.idle = self.createImages(self.basePath+'/textures/enemy/idleAni/0.png')
        self.search = False
        self.speed = 0.01

    @property
    def npcPos(self):
        return (int(self.x), int(self.y))

    #fix movement!
    def npcMovement(self):
        nextPos = self.game.path.creatPath(self.npcPos, self.game.player.player_pos_map)
        dx, dy = nextPos[0]-self.x, nextPos[1]-self.y
        angle = atan2(dy+0.5, dx+0.5)
        cos_a = cos(angle)
        sin_a = sin(angle)

        tryX = self.speed * cos_a
        tryY = self.speed * sin_a

        if self.checkWall(self.x, self.y+tryY):
            self.y += tryY
        if self.checkWall(self.x + tryX, self.y):
            self.x += tryX

    def checkWall(self, x, y):
        if not (x, y) in self.game.map.walls:
            return True
        return False

    def npcRay(self):
        if self.game.player.player_pos_map == (int(self.x), int(self.y)):
            return True
        
        player_x, player_y = self.game.player.player_pos
        delta_x, delta_y = player_x - self.x, player_y - self.y
        a = atan2(delta_y, delta_x)+1e-6
        cos_a = cos(a)
        sin_a = sin(a)

        #Vertical
        x_vert,dx = (int(self.x)+1, 1) if cos_a > 0 else (int(self.x)-1e-6, -1)
        depth_vert = (x_vert-self.x)/cos_a
        y_vert = self.y + depth_vert*sin_a
        del_depth = dx / cos_a
        dy = del_depth * sin_a
        player_verts = 0
        wall_verts = 0

        for _ in range(MAX_DEPTH):
            vert_coords = int(x_vert), int(y_vert)
            # print(vert_coords)
            if vert_coords == self.game.player.player_pos_map:
                player_verts = depth_vert
                break
            if vert_coords in self.game.map.walls:
                wall_verts = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += del_depth

        #Horz
        y_horz, dy = (int(self.y)+1, 1) if sin_a > 0 else (int(self.y)-1e-6, -1)
        depth_horz = (y_horz-self.y)/sin_a
        x_horz = self.x + depth_horz*cos_a
        del_depth = dy / sin_a
        dx = del_depth * cos_a
        player_horz = 0
        wall_horz = 0

        for _ in range(MAX_DEPTH):
            horz_coords = int(x_horz), int(y_horz)
            if horz_coords == self.game.player.player_pos_map:
                player_horz = depth_horz
                break
            if horz_coords in self.game.map.walls:
                wall_horz = depth_horz
                # print("found wall")
                break
            x_horz += dx
            y_horz += dy
            depth_horz += del_depth

        player_depth = max(player_horz, player_verts)
        wall_depth = max(wall_horz, wall_verts)

        if 0 < player_depth < wall_depth or wall_depth == 0:
            return True

        return False

    def update(self):
        # super().update()
        self.check_animation_time()
        self.render()
        self.npcLogic()

    def npcLogic(self):
        if self.npcRay():
            self.search = True
            self.npcMovement()
        else:
            self.switch_img(self.idle)
