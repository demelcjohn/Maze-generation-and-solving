import random
import numpy as np
from displayMaze import displayMaze

isEnd = False


def okneighbours(maze, i, j, n, m):
    count = 0
    if (j != 0 and (maze[i][j-1] == 0)):
        count += 1
    if (i != 0 and (maze[i-1][j] == 0)):
        count += 1
    if (j != m-1 and (maze[i][j+1] == 0)):
        count += 1
    if (i != n-1 and (maze[i+1][j] == 0)):
        count += 1
    return count


def gen(maze, i, j, n, m):

    nei = okneighbours(maze, i, j, n, m)

    if (i == n-1 and j == m-1) or nei < 2:
        return maze


n = 20  # int(input())
m = 30  # int(input())
maze = np.empty((n, m), dtype=int)
maze = np.zeros((n, m))
maze = maze.astype(int)

maze = gen(maze, 0, 0, n, m)
displayMaze(maze)

# d = 0
# r = 0
# for i in range(n+m):
#     random_int = random.randint(0, 1)
#     if random_int == 0:
#         d += 1
#         maze[d][r] = 1
#     if random_int == 1:
#         r += 1


# S-####################
# -####################
# ------###-###########
###### --##-#######-###
####### -##-##------###
####### ----##-####-###
####### -##----####-###
# ---E
