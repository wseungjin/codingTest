
def solution(board):
    N = len(board[0])
    answer = 0
    square = [[0 for i in range(N)]] * N
    for i in range(N):
        for j in range(N):
            if(board[i][j] ==1 ):
                square[i][j] = -1
                
    for n in range(N):
        for i in range(n):
            for j in range(n):
                if(square[i+1][j]!=-1):
                    square = square[i][j] + 100
                
                
    
    print(square)
                

    return answer
    
    
def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]	
    print(solution(board))
    
main()