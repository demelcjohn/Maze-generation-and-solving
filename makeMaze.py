import os
import random
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
    else:
        _ = os.system('clear')


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
            print(nei)
            nIndex = neighbour[nei]
            flag = 0
            if curr[0]+nIndex[0] != -1 and curr[1]+nIndex[1] != -1 and curr[0]+nIndex[0] != n-1 and curr[1]+nIndex[1] != m-1:
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
    return maze


def checkNeighbours(maze, x, y, n):
    print(x, y)
    count = 0
    for i in (-1, 1):
        for j in (-1, 1):
            if (maze[x+i][y+j] == 1):
                count += 1
    if count > n:
        return False
    else:
        return True
