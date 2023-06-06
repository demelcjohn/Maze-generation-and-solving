import copy
import os
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
    while not (curr[0] == n-1 and curr[1] == m-1):
        nei = getNeighbour(maze, curr)
        print(nei)
        if nei != (-1, -1):
            curr = nei
            maze[curr[0]][curr[1]] = 2
            stack.append(curr)
        else:
            maze[curr[0]][curr[1]] = 3
            curr = stack.pop()
        clear_terminal()
        displayMaze(maze)
        print()
        displayMaze(mazeReal)
        # print("\n", maze)
    displayMaze(maze)


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
