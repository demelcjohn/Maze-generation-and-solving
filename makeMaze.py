import random
import numpy as np
from displayMaze import displayMaze

stack = []
neighbour = {
    0: (-1, -1),
    1: (-1, 1),
    2: (1, -1),
    3: (1, 1)
}


def makeMaze(n, m):
    maze = np.empty((n, m), dtype=int)
    maze = np.zeros((n, m))
    maze = maze.astype(int)
    displayMaze(maze)

    maze = correctWay(maze)


def correctWay(maze):
    n, m = maze.shape
    curr = (0, 0)
    maze[0][0] = 1
    stack.append(curr)
    while curr != (n-1, n-1):
        okneighbours = [0, 1, 2, 3]
        while True:
            nei = random.choice(okneighbours)
            nIndex = neighbour[nei]
            print(nIndex)
            if maze[curr[0]+nIndex[0]][curr[1]+nIndex[1]] == 0:
                if checkNeighbours(maze, curr[0]+nIndex[0], curr[1]+nIndex[1]):
                    curr = (curr[0]+nIndex[0], curr[1]+nIndex[1])
                    stack.append(curr)
                    break
            else:
                okneighbours.pop(nei)
            if okneighbours == []:
                stack.pop()
                curr = stack[-1]
                break


def checkNeighbours(maze, x, y):
