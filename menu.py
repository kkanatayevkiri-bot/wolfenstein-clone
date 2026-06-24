import pygame
from button import *

class Menu:
    def __init__(self,engine):
        self.engine = engine
        self.done = False
        self.next = "game"
        self.curr = "menu"
        self.btns = []
        creat_btns = self.creat_btns
        creat_btns(Button(self.engine, (255,255,255), "Start",-200, "play"))
        creat_btns(Button(self.engine, (255,255,255), "Settings",0, "settings"))
        creat_btns(Button(self.engine, (255,255,255), "Quit",200, "quit"))

    def creat_btns(self, btn):
        self.btns.append(btn)

    def input(self,event):
        mouse_pos = pygame.mouse.get_pos()# A tuple

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.engine.running = False

        for btn in self.btns:
            if btn.btn_size.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                #the reason we do not call collidepoint into the 'mouse_pos' but into
                #BUT ONE RECTS (or shaps) ONLY!!
                if btn.action == "quit":
                    self.engine.running = 0
                elif btn.action == "play":
                    self.done = True

    def update(self):pass

    def draw(self):
        self.engine.window.fill((100,0,0))
        for btn in self.btns:
            btn.draw()