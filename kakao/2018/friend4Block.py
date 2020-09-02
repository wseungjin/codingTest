import re
def isDeleted(col,row,board):
    if(board[col][row] != -1 and board[col][row] == board[col][row+1] and board[col][row+1] == board[col+1][row] and board[col][row+1] == board[col+1][row+1]):
        return True
    return False
def getDelete(board):
    willBeDeleted = set()
    for col in range(len(board) -1 ):
        for row in range(len(board[col]) -1 ):
            if(isDeleted(col,row,board)):
                willBeDeleted.add((col,row))
                willBeDeleted.add((col,row+1))
                willBeDeleted.add((col+1,row))
                willBeDeleted.add((col+1,row+1))
    return willBeDeleted

def delete(board,willBeDeleted):
    for element in willBeDeleted:
        board[element[0]][element[1]] = -1
    
def makeNewOrder(nowOrder):    
    count = 0
    i = 0
    while i < len(nowOrder):
        if nowOrder[i] == -1 :
            nowOrder.pop(i)
            count = count + 1
        else :
            i = i + 1          
    for j in range(count):
        nowOrder.append(-1)  
    return nowOrder
    
def down(board):
    for row in range(len(board[0])):
        nowOrder = []
        for col in range(len(board)-1 , -1 , -1):
            nowOrder.append(board[col][row])
        newOrder = makeNewOrder(nowOrder)
        for col in range(len(board)-1 , -1 , -1):
            board[col][row] = newOrder[len(board)-1-col]
            
def printBoard(board):
    for col in range(len(board)):
        print(board[col])
    
def solution(m, n, board):    
    regex = re.compile(r'\w')
    for i in range(len(board)):
        board[i] = regex.findall(board[i])

    answer = 0
    willBeDeleted = getDelete(board)
    while(len(willBeDeleted) != 0 ):
        answer = answer + len(willBeDeleted)
        delete(board,willBeDeleted)
        down(board)
        willBeDeleted = getDelete(board)
    return answer

def main():
    print(solution(4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

main()