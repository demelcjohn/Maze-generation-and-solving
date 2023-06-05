import numpy as np
from displayMaze import displayMaze

stack = []


def makeMaze(n, m):
    maze = np.empty((n, m), dtype=int)
    maze = np.zeros((n, m))
    maze = maze.astype(int)
    displayMaze(maze)

    maze = correctWay(maze)


def correctWay(maze):
    n, m = maze.shape
    curr = (0, 0)
    stack.append(curr)
    while curr != (n-1, n-1):
        print("hello")
        curr = (n-1, n-1)
