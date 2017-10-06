def nextMove(n,r,c,grid):
    for i in range(0, n):
        if grid[i].find('p') > -1:
            pr = i
            pc = grid[i].find('p')
    vertical = r - pr
    horizontal = c - pc
    if(vertical != 0):
        if vertical > 0:
            print("UP")
        else:
            print("DOWN")
    elif (horizontal != 0):
        if horizontal > 0:
            print("LEFT")
        else:
            print("RIGHT")

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

nextMove(n,r,c,grid)