from displayMaze import displayMaze


stack = []


def solveMaze(maze):
    n, m = maze.shape
    curr = (0, 0)
    maze[curr[0]][curr[1]] = 2
    stack.append(curr)
    while curr[0] != n-1 and curr[1] != m-1:
        nei = getNeighbour(maze, curr)
        if nei == (-1, -1):
            maze[curr[0]][curr[1]] = 1
            stack.pop()
        else:
            curr = nei
            maze[curr[0]][curr[1]] = 2
            stack.append(curr)
        displayMaze(maze)


def getNeighbour(maze, pos):
    n, m = maze.shape
    x, y = pos
    if x >= 0:
        if maze[x-1][y] == 1:
            return (x-1, y)
    if y >= 0:
        if maze[x][y-1] == 1:
            return (x, y-1)
    if x < n:
        if maze[x+1][y] == 1:
            return (x+1, y)
    if y < m:
        if maze[x][y+1] == 1:
            return (x, y+1)
    return (-1, -1)
