class correctWay:
    def __init__(self, cell, neighbours):
        self.cell = cell
        self.neighbours = neighbours


stack = []


def solveMaze(maze):
    n, m = maze.shape
    curr = (0, 0)
    neighbours = getNeighbours(maze, curr)
    way = correctWay(curr, neighbours)
    stack.append(way)
    while curr[0] != n-1 and curr[1] != m-1:
        print("Hello")


def getNeighbours(maze, x, y):
    n, m = maze.shape
    nei = []
    if x >= 0:
        if maze[x-1][y] == 1:
            nei.append((x, y))
    if y >= 0:
        if maze[x][y-1] == 1:
            nei.append((x, y))
    if x < n:
        if maze[x+1][y] == 1:
            nei.append((x, y))
    if y < m:
        if maze[x][y+1] == 1:
            nei.append((x, y))
    return nei
