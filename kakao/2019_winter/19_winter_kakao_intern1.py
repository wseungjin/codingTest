def solution(board, moves):
    
    n = len(board[0])
    
    level = [0]*n
    answer = 0
    
    stack = []
    
    for row in range(n):
        eachLevel = 0
        for column in range(n):
            if(board [column][row]!=0):
                eachLevel= eachLevel + 1
            
        level[row]= eachLevel
        
    moveNumber = len(moves)
    curStack=0 
    
    for i in range(moveNumber):
        currentRow=moves[i]-1
        if level[currentRow] != 0 :
            currentDoll=board[n-1-(level[currentRow]-1)][currentRow]
            if(currentDoll!=0):
                if(curStack!=0):
                    if (stack[curStack-1] == currentDoll):
                        answer = answer + 2
                        stack.pop()
                        curStack= curStack -1 
                    else : 
                        stack.append(currentDoll)
                        curStack= curStack +1  

                else: 
                    stack.append(currentDoll)
                    curStack= curStack +1  
                board[n-1-(level[currentRow]-1)][currentRow] = 0
                level[currentRow] = level[currentRow] -1 
    
    return answer


def main():
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]	
    
    print(solution(board,moves))
    
main()