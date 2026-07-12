from collections import deque

class FindPath:
    def __init__(self, game):
        #  MAP, self.map.walls
        self.game = game
        self.m = self.game.map.map
        self.moves = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)]
        # self.moves = [(1,0),(-1,0),(0,1),(0,-1)]
        self.graph = self.creatGraph()
        # print((3,4) in self.game.map.walls)

    #Graph creation
    def graphMoves(self, x, y):
        return [(x+dx, y+dy) for dx, dy in self.moves if (x+dx, y+dy) not in self.game.map.walls]

    def creatGraph(self):
        d = {}
        for y, row in enumerate(self.m):
            for x, col in enumerate(row):
                if col==0:
                    d[(x,y)] = self.graphMoves(x,y)
        return d

    def creatPath(self, npc, player):
        if npc == player:
            return npc

        visited = set()
        queu = deque()
        path = {}

        visited.add(npc)
        queu.append(npc)

        while queu:
            curr_node = queu.popleft()
            if curr_node == player:
                break
            for node in self.graph[curr_node]:
                if node not in visited:
                    path[node] = curr_node
                    visited.add(node)
                    queu.append(node)

        #fix path
        fixed_path = []
        curr = player
        while curr != npc:
            fixed_path.append(curr)
            curr = path[curr]
        fixed_path.reverse()
        return fixed_path[0]

        


# if __name__ == "__main__":
#     MAP = [[1,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,0,1],
#     [1,0,0,0,0,0,0,1],
#     [1,0,0,1,1,0,0,1],
#     [1,0,0,1,1,0,0,1],
#     [1,0,0,0,0,0,0,1],
#     [1,0,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1,1],]

#     p = (5,4)
#     e = (6,6)
#     def findWalls(m):
#         d = {}
#         for row in range(len(m)):
#             for col in range(len(m[row])):
#                 if m[row][col]:
#                     d[(row,col)]=1
#         return d

#     walls = findWalls(MAP)
#     test = FindPath(MAP,walls)
#     print(test.creatPath(e, p))