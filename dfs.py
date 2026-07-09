from collections import deque

class FindPath:
    def __init__(self, game):
        #  MAP, self.map.walls
        self.game = game
        self.m = self.game.map.map
        self.walls = self.game.map.walls

        self.graph = self.creatGraph(self.m)

    #Graph creation
    def graphMoves(self, r, c):
        moves = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)]
        return [(r+dx, c+dy) for dx, dy in moves if (r+dx, c+dy) not in self.walls]

    def creatGraph(self, m):
        d = {}
        for row in range(len(m)):
            for col in range(len(m[row])):
                if m[row][col] == 0:
                    d[(row,col)] = self.graphMoves(row, col)

        return d

    def creatPath(self, curr_pos, player):
        if curr_pos == player:
            return curr_pos

        visited = set()
        queu = deque()
        path = {}

        visited.add(curr_pos)
        queu.append(curr_pos)

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
        while curr != curr_pos:
            fixed_path.append(curr)
            curr = path[curr]
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