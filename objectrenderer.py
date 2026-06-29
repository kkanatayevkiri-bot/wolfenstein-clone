from settings import*
import pygame
import os

class Objectrenderer:
    def __init__(self, game):
        self.basePath = os.path.dirname(os.path.abspath(__file__))
        self.game = game
        self.screen = game.engine.window
        self.walls = self.load_wall_textures()
        self.ground = (92, 64, 51)
        self.sky = pygame.image.load(os.path.join(self.basePath ,'textures/background/skyBG.webp')).convert_alpha()
        self.sky = pygame.transform.scale(self.sky,(X,HALF_Y))

    def draw(self):
        self.drawBg()
        self.render_walls()

    def drawBg(self):
        offset = self.game.player.PLAYER_A * ROTATE_SPEED
        self.screen.blit(self.sky,(offset,0))
        self.screen.blit(self.sky,(-X+offset,0))
        pygame.draw.rect(self.screen,self.ground,(0,Y//2,X,Y//2))

    @staticmethod
    def get_texture(file_path, size=(TEX_SIZE, TEX_SIZE)):
        texture = pygame.image.load(file_path).convert_alpha()
        return pygame.transform.scale(texture, size)

    def load_wall_textures(self):
        return {1:self.get_texture('/home/kirill/code/python/games/tests/textures/walls/0.png')}

    def render_walls(self):
        walls = self.game.rays.wall_results
        walls = sorted(walls, key=lambda walls: walls[2], reverse=True)

        # wall_slice,wall_pos,depth
        for wall_slice, wall_pos, depth in walls:
            self.screen.blit(wall_slice, wall_pos)