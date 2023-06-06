def displayMaze(maze):
    n, m = maze.shape
    for i in range(m+2):
        print("#", end=" ")
    print()
    for i in range(n):
        print("#", end=" ")
        for j in range(m):
            if i == 0 and j == 0:
                print("S", end=" ")
            elif i == n-1 and j == m-1:
                print("E", end=" ")
            elif maze[i][j] == 0:
                print("#", end=" ")
            elif maze[i][j] == 1:
                print("-", end=" ")
            elif maze[i][j] == 2:
                print("*", end=" ")
        print("#")
    for i in range(m+2):
        print("#", end=" ")
    print()
