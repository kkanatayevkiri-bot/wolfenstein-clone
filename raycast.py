from settings import*
from math import cos, sin
import pygame

class Raycasting:
    def __init__(self, game, engine=None):
        self.game = game
        # self.engine = engine
        self.textures_dict = self.game.object_renderer.walls
        self.ray_results = []
        self.wall_results = []

    def wall_data(self):
        self.wall_results = []
        for ray, data in enumerate(self.ray_results):
            texture, offset, wall_height, depth = data
            if wall_height < Y:
                wall_slice = self.textures_dict[texture].subsurface((TEX_SIZE-2)*offset, 0, SCALE, TEX_SIZE)
                wall_slice = pygame.transform.scale(wall_slice,(SCALE, wall_height))
                wall_pos = (ray*SCALE, HALF_Y - wall_height//2)
                self.wall_results.append((wall_slice,wall_pos,depth))
            else:
                ratio = Y / wall_height
                h = TEX_SIZE * ratio
                y_point = TEX_SIZE_HALF - h/2
                wall_slice = self.textures_dict[texture].subsurface((TEX_SIZE-2)*offset, y_point, SCALE, h)
                wall_slice = pygame.transform.scale(wall_slice,(SCALE, Y))
                wall_pos = (ray*SCALE, 0)
                self.wall_results.append((wall_slice,wall_pos,depth))


            # print(f"{self.wall_results}")

    def cast_ray(self):
        self.ray_results = []
        px, py = self.game.player.player_pos
        x_map, y_map = self.game.player.player_pos_map
        ray_a = self.game.player.PLAYER_A - FOV_HALF+0.0001
        for ray in range(NUM_RAYS):
            cos_a = cos(ray_a)
            sin_a = sin(ray_a)

            #Vertical
            x_vert,dx = (x_map+1, 1) if cos_a > 0 else (x_map-1e-6, -1)
            depth_vert = (x_vert-px)/cos_a
            y_vert = py + depth_vert*sin_a
            del_depth = dx / cos_a
            dy = del_depth * sin_a

            for _ in range(MAX_DEPTH):
                vert_coords = int(x_vert), int(y_vert)
                if vert_coords in self.game.map.walls:
                    vert_tex = self.game.map.walls[vert_coords]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += del_depth

            #Horz
            y_horz, dy = (y_map+1, 1) if sin_a > 0 else (y_map-1e-6, -1)
            depth_horz = (y_horz-py)/sin_a
            x_horz = px + depth_horz*cos_a
            del_depth = dy / sin_a
            dx = del_depth * cos_a

            for _ in range(MAX_DEPTH):
                horz_coords = int(x_horz), int(y_horz)
                if horz_coords in self.game.map.walls:
                    horz_tex = self.game.map.walls[horz_coords]
                    break
                x_horz += dx
                y_horz += dy
                depth_horz += del_depth


            if depth_vert < depth_horz:
                offset, texture = y_vert%1 if cos_a>0 else 1-(y_vert%1), vert_tex
                depth = depth_vert
            else:
                offset, texture = 1-(x_horz%1) if sin_a>0 else x_horz%1, horz_tex
                depth = depth_horz

            depth*=cos(self.game.player.PLAYER_A-ray_a)
            wall_height = DISTANCE / depth+0.0001
            #debug tool
            # pygame.draw.rect(self.engine.window, ('white'), (ray*SCALE, HALF_Y - wall_height//2, SCALE, wall_height))
            self.ray_results.append((texture,offset,wall_height,depth))
            # print(f"{texture} {offset} {wall_height} {depth}")
            ray_a += DEL_RAY

    def update(self):
        self.cast_ray()
        self.wall_data()
