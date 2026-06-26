from objectsAnimated import*
from settings import*
import pygame

class Weapons(ObjectsAnimated):
    def __init__(self, game, path="/textures/shotgun/0.png", animation_time=60,scale=3):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.l_imgs = deque(
            [pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale)) for img in self.l_imgs]
            )
        self.image = self.l_imgs[0]
        self.pos = HALF_X-self.image.get_width()/2, Y-self.image.get_height()
        self.imgs_len = len(self.l_imgs)
        self.curr_i = 0
        self.reload = False

    def commandReload(self):
        if self.game.player.shot:
            self.reload = True
            self.game.player.shot = False

        if self.reload and self.curr_i < self.imgs_len and self.animation_trigger:
            self.curr_i+=1
            self.l_imgs.rotate(-1)
            self.image = self.l_imgs[0]

        if self.curr_i == self.imgs_len:
            self.curr_i = 0
            self.reload = False

    def update(self):
        self.check_animation_time()
        self.commandReload()

    def draw(self, screen):
        screen.blit(self.image, self.pos)
