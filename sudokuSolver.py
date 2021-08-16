




def sudokuSolver(board,depth = 0):
    
    newBoard =[]
    for row in board:
        newBoard.append(row.copy())
    size = len(newBoard)
    emptyCol = -1
    emptyRow = -1
    broken = False
    for row in range(len(newBoard)):
        for col in range(len(newBoard[0])):
            if newBoard[row][col]==" ":
                emptyRow = row
                emptyCol = col
                broken = True
                break
        if broken:
            break
    if emptyCol==-1:
        return newBoard
    else:
        
        for i in range(1,size+1):
            newNewBoard = newBoard.copy()
            isOkPlace = checkPlacement(newNewBoard,emptyRow,emptyCol,str(i))
            if isOkPlace:
                #print(depth)
                #print(newNewBoard)
                #if newNewBoard!=board:
                    #print("error")
                
                newNewBoard[emptyRow][emptyCol] = str(i)
                
                returnedBoard = sudokuSolver(newNewBoard,depth+1)
                
                if returnedBoard!=None:
                    
                    return returnedBoard
    #if newNewBoard!=board:
       # print("error")
    #print(depth)
    return None

def checkPlacement(board,row,col,num):
    size = len(board)
    for item in board[row]:
        if item==num:
            return False
    for ind in range(len(board)):
        if board[ind][col]==num:
            return False
    boxR = int(row//(size**.5)*(size**.5))
    boxC = int(col//(size**.5)*(size**.5))
    for r in range(boxR,boxR+3):
        for c in range(boxC,boxC+3):
            if board[r][c]==num:
                return False

    return True


def printBoard(board):
    print("-"*(len(board[0])*2+1))
    for r in range(len(board)):
        print("|",end="")
        for c in range(len(board[0])):
            ender = " "
            if (c+1)%((len(board))**0.5)==0:
                ender = "|"
            print(board[r][c],end=ender)
        print()
        if (r+1)%((len(board))**0.5)==0:
            print("-"*(len(board[r])*2+1))



row123 = [[" ","6"," ","4"," ","5"," "," "," "],[" "," "," "," "," "," ","4"," "," "],["3","7"," "," "," "," "," "," ","6"]]
row456 = [[" ","3","1","6"," "," "," "," "," "],[" "," "," ","8","3"," "," "," "," "],[" "," "," "," ","4"," "," "," ","1"]]
row789 = [[" "," ","3","2"," "," "," "," "," "],["4"," "," "," "," "," ","8"," "," "],[" ","1","8"," "," ","6","7","5"," "]]
board = row123+row456+row789
emptyBoard = [[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "]]
printBoard(board)
printBoard(sudokuSolver(board))



     
