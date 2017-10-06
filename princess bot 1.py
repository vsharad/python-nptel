def displayPathtoPrincess():
    m = int(input())
    grid = []
    for i in range(0, m): 
        grid.append(input().strip())
        if grid[i].find('m') > -1:
            mr = i
            mc = grid[i].find('m')
        if grid[i].find('p') > -1:
            pr = i
            pc = grid[i].find('p')
    vertical = mr - pr
    horizontal = mc - pc
    while(vertical != 0):
        if vertical > 0:
            print("UP")
            vertical -= 1
        else:
            print("DOWN")
            vertical += 1
    while(horizontal != 0):
        if horizontal > 0:
            print("LEFT")
            horizontal -= 1
        else:
            print("RIGHT")
            horizontal += 1

displayPathtoPrincess()
