def manhattan_distance(pos,board):
    #get all the dust positions
    dust = [(rnum,i) for rnum,row in enumerate(board) for i,x in enumerate(row) if x=='d']
    manhattan_distance = [abs(pos[0]-end[0])+abs(pos[1]-end[1]) for end in dust]
    #print(manhattan_distance)
    if len(manhattan_distance) > 0:
        closest = manhattan_distance.index(min(manhattan_distance))
        return dust[closest]

# Head ends here
def next_move(posr, posc, board):
    closest = manhattan_distance([posr,posc],board)
    if(closest != None):
        (pr,pc) = closest
        vertical = posr - pr
        horizontal = posc - pc
        if(vertical != 0):
            if vertical > 0:
                posr -= 1
                print("UP")
            else:
                posr += 1
                print("DOWN")
        elif (horizontal != 0):
            if horizontal > 0:
                posc -= 1
                print("LEFT")
            else:
                posc += 1
                print("RIGHT")
        else:
            board[posr][posc] = '-'
            print("CLEAN")
            #print(board)
        #next_move(posr,posc,board)

pos = [0,0]
board = [['b', '-', '-', '-', '-'], ['d', '-', '-', 'd', '-'], ['d', '-', '-', '-', '-'], ['d', '-', '-', '-', '-'], ['d', '-', '-', '-', '-']]
next_move(pos[0], pos[1], board)
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)




