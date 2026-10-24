from npc import *
from objects import *
from objectsAnimated import *
import pygame

class ObjectHandeler:
    def __init__(self, game, engine):
        self.engine = engine
        self.game = game

        self.npcLis = []
        self.npcPositions = []
        self.objectsLis = []
        addNpc = self.addNpc
        addObjs = self.addObjs

        addNpc(Npc(game, pos=(6.5,8.5)))
        addNpc(Npc(game, pos=(6.5,1.5)))

        addObjs(Objects(game))
        addObjs(ObjectsAnimated(game))

        self.last_ticks = pygame.time.get_ticks()

    def removeDead(self):
        curr = pygame.time.get_ticks()
        if curr - self.last_ticks >= 5000:
            self.last_ticks = curr
            return True
        return False

    def findNpcPos(self):
        self.npcPositions = [npc.npcPos for npc in self.npcLis]

    def addNpc(self, npc):
        self.npcLis.append(npc)
     
    def addObjs(self, obj):
        self.objectsLis.append(obj)

    def update(self):
        [npc.update() for npc in self.npcLis]
        if self.removeDead():
            self.npcLis = [npc for npc in self.npcLis if npc.alive]
        # self.findNpcPos()
        [obj.update() for obj in self.objectsLis]