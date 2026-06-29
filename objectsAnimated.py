from objects import Objects
from collections import deque
import pygame
import os

class ObjectsAnimated(Objects):
    def __init__(self,game , pos=(5.5,5.5) ,path='/textures/objectsAni/0.png' ,animation_time=90 , offset=0.27, scale=0.5):
        super().__init__(game, path, pos, offset, scale)
        self.animation_time = animation_time
        self.l_imgs = self.createImages(self.basePath+path)
        self.last_time = pygame.time.get_ticks()
        self.animation_trigger = False

    def switch_img(self, imgs):
        if self.animation_trigger:
            imgs.rotate(-1)
            self.image = imgs[0]

    def check_animation_time(self):
        self.animation_trigger = False
        curr_time = pygame.time.get_ticks()
        if curr_time - self.last_time >= self.animation_time:
            self.last_time = curr_time
            self.animation_trigger = True

    def createImages(self, path):
        l = deque()
        path = path.rsplit('/',1)[0]
        for file in os.listdir(path):
            img = pygame.image.load(os.path.join(path, file)).convert_alpha()
            l.append(img)
        return l

    def update(self):
        super().update()
        self.check_animation_time()
        self.switch_img(self.l_imgs)