import copy
import os
import time
from displayMaze import displayMaze


stack = []


def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')


def solveMaze(maze):
    mazeReal = copy.copy(maze)
    n, m = maze.shape
    curr = (0, 0)
    maze[curr[0]][curr[1]] = 2
    stack.append(curr)
    inside = 1
    while not (curr[0] == n-1 and curr[1] == m-1):
        if maze[curr[0]][curr[1]] == 2 and inside ==0:
            stack.append(curr)
        nei = getNeighbour(maze, curr)
        print(nei)
        if nei != (-1, -1):
            curr = nei
            maze[curr[0]][curr[1]] = 2
            stack.append(curr)
            inside = 1
        else:
            maze[curr[0]][curr[1]] = 3
            curr = stack.pop()
            inside = 0
        clear_terminal()
        displayMaze(maze)
        print()
        displayMaze(mazeReal)
        # print(stack)
        # time.sleep(1)
    print(stack)
        


def getNeighbour(maze, pos):
    n, m = maze.shape
    x, y = pos
    if x > 0:
        if maze[x-1][y] == 1:
            return (x-1, y)
    if y > 0:
        if maze[x][y-1] == 1:
            return (x, y-1)
    if x < n-1:
        if maze[x+1][y] == 1:
            return (x+1, y)
    if y < m-1:
        if maze[x][y+1] == 1:
            return (x, y+1)
    return (-1, -1)
