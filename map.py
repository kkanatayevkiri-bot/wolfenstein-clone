import pygame

MAP = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,1,1,0,0,1],
    [1,0,0,1,1,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
    ]

class Map:
    def __init__(self, engine):
        self.engine = engine
        self.map = MAP
        self.walls = self.find_walls()

    def find_walls(self):
        d = {}
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if self.map[y][x]:
                    d[(x, y)] = 1
        return d

    # def draw(self):
    #     for x,y in self.walls:
    #         pygame.draw.rect(self.engine.window,(255,255,255),(x*100,y*100,100,100),2)
    

# if __name__ == "__main__":
#     t = Map(1)
#     print(t.walls)
#     t.draw()


