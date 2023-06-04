import numpy as np
from displayMaze import displayMaze


def makeMaze(n, m):
    maze = np.empty((n, m), dtype=int)
    maze = np.zeros((n, m))
    maze = maze.astype(int)

    displayMaze(maze)
