import random
import numpy as np
from displayMaze import displayMaze
from makeMaze import makeMaze
from solveMaze import solveMaze


print("\nMaze Generation and Solving \n")
n =  int(input("Enter number of rows : "))
m =  int(input("Enter number of columns : "))
maze = makeMaze(n, m)
input()

solveMaze(maze)



