import pygame
from settings import *
class Button:
    def __init__(self,engine,color,text, offset, action):
        self.engine = engine
        self.action = action
        # self.font = pygame.font.SysFont("Arial", 72)
        self.font = pygame.font.SysFont("Arial", 72)
        self.text_surface = self.font.render(text, True, color,)
        self.txt_rect = self.text_surface.get_rect() #<--- SHAPE 
        self.txt_rect.center = (X//2,Y//2+offset)
        self.btn_size = pygame.Rect(0,0,self.text_surface.get_width()+50,self.text_surface.get_height()+50)
        self.btn_size.center =  self.txt_rect.center

    def draw(self):
        pygame.draw.rect(self.engine.window,(100,50,50),self.btn_size)
        self.engine.window.blit(self.text_surface, self.txt_rect)