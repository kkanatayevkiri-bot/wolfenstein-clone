from npc import *
from objects import *
from objectsAnimated import *

class ObjectHandeler:
    def __init__(self, game):
        self.game = game

        self.npcLis = []
        self.npcPositions = []
        self.objectsLis = []
        addNpc = self.addNpc
        addObjs = self.addObjs

        addNpc(Npc(game))
        addNpc(Npc(game, pos=(1.5,4.5)))

        addObjs(Objects(game))
        addObjs(ObjectsAnimated(game))

    def findNpcPos(self):
        self.npcPositions = [npc.npcPos for npc in self.npcLis]

    def addNpc(self, npc):
        self.npcLis.append(npc)
     
    def addObjs(self, obj):
        self.objectsLis.append(obj)

    def update(self):
        [npc.update() for npc in self.npcLis]
        # self.findNpcPos()
        [obj.update() for obj in self.objectsLis]