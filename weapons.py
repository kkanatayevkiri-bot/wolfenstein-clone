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
        self.x, self.y = HALF_X-self.image.get_width()/2, Y-self.image.get_height()+10
        self.ogY = self.y
        self.imgs_len = len(self.l_imgs)
        self.curr_i = 0
        self.reload = False
        self.wpDmg = 50

    def commandReload(self):
        if self.game.player.shot and not self.reload:
            self.reload = True
            self.game.player.shot = False

        if self.reload and self.animation_trigger:
            self.l_imgs.rotate(-1)
            self.image = self.l_imgs[0]
            self.curr_i+=1

            if self.curr_i == self.imgs_len:
                self.curr_i = 0
                self.reload = False

    def update(self):
        self.check_animation_time()
        self.commandReload()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.line(screen,(255,0,0),(HALF_X,HALF_Y-10),(HALF_X,HALF_Y+10))
        pygame.draw.line(screen,(255,0,0),(HALF_X-10,HALF_Y),(HALF_X+10,HALF_Y))


class MachineGun(Weapons):
    def __init__(self, game, path="/textures/machineGun/0.png" ,animation_time=60, scale=3):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.wpDmg = 25