def find_dust(board):
    dust_position = [(rnum,cnum) for rnum,row in enumerate(board) for cnum,element in enumerate(row) if element=='d']
    return dust_position

def nextMove(posr, posc, board):
    

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
