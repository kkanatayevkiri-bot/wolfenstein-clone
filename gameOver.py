import pygame
from button import *

class GameOver:
    def __init__(self, statemanager, engine):
        self.engine = engine
        self.stateM = statemanager
        self.done = False
        self.next = "game"
        self.curr = "gameover"
        self.btns = []
        creat_btns = self.creat_btns
        creat_btns(Button(self.engine, (255,255,255), "Try Again!?",-200, "op1"))
        # creat_btns(Button(self.engine, (255,255,255), "Settings",0, "settings"))
        creat_btns(Button(self.engine, (255,255,255), "Quit To Menu",200, "op2"))

    def creat_btns(self, btn):
        self.btns.append(btn)

    def input(self,event):
        mouse_pos = pygame.mouse.get_pos()# A tuple

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.done = True

        for btn in self.btns:
            if btn.btn_size.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                #the reason we do not call collidepoint into the 'mouse_pos' but into
                #BUT ONE RECTS (or shaps) ONLY!!
                if btn.action == "op1":
                    self.next = "game"
                elif btn.action == "op2":
                    self.next = "menu"
                self.done = True

    def update(self):pass

    def draw(self):
        self.engine.window.fill((155,0,0))
        for btn in self.btns:
            btn.draw()