import random
import numpy as np


n = 3  # int(input())
m = 4  # int(input())
maze = np.empty((n, m), dtype=int)
maze = np.zeros((n, m))
print(maze)
maze = maze.astype(int)

d = 0
r = 0
for i in range(n+m):
    random_int = random.randint(0, 1)
    if random_int == 0:
        d += 1
        maze[d][r] = 1
    if random_int == 1:
        r += 1
