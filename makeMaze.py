import os
import random
import time
import numpy as np
from displayMaze import displayMaze

stack = []
neighbour = {
    0: (-1, 0),
    1: (0, -1),
    2: (1, 0),
    3: (0, 1)
}


def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')


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
    while curr != (n-1, m-1):
        okneighbours = [0, 1, 2, 3]
        while True:
            nei = random.choice(okneighbours)
            nIndex = neighbour[nei]
            flag = 0
            if curr[0]+nIndex[0] != -1 and curr[1]+nIndex[1] != -1 and curr[0]+nIndex[0] != n and curr[1]+nIndex[1] != m:
                if maze[curr[0]+nIndex[0]][curr[1]+nIndex[1]] == 0:
                    if checkNeighbours(maze, curr[0]+nIndex[0], curr[1]+nIndex[1], 1):
                        flag = 1
                        curr = (curr[0]+nIndex[0], curr[1]+nIndex[1])
                        stack.append(curr)
                        maze[curr[0]][curr[1]] = 1
                        break
            if flag == 0:
                okneighbours.remove(nei)
            if okneighbours == []:
                stack.pop()
                curr = stack[-1]
                break
        clear_terminal()
        displayMaze(maze)
        print("\n", maze)
        # time.sleep(1)
    return maze


def checkNeighbours(maze, x, y, val):
    n, m = maze.shape
    count = 0
    for i in range(2):
        for j in (-1, 1):
            if (x+i < n) and (y+j < m):
                if i == 0:
                    if (maze[x][y+j] == 1):
                        count += 1
                if i == 1:
                    if (maze[x+j][y] == 1):
                        count += 1
    if count > val:
        return False
    else:
        return True
