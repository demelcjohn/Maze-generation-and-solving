import random
import numpy as np
from displayMaze import displayMaze
from makeMaze import makeMaze
from solveMaze import solveMaze


n = 20  # int(input())
m = 30  # int(input())
maze = makeMaze(n, m)
solveMaze(maze)


# S-####################
# -####################
# ------###-###########
###### --##-#######-###
####### -##-##------###
####### ----##-####-###
####### -##----####-###
# ---E
