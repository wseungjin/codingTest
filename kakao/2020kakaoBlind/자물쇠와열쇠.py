import copy

def isSolved(solvedLock):
    for lockCol in range(len(solvedLock)):
        for lockRow in range(len(solvedLock)):
            if (solvedLock[lockCol][lockRow]!=1):
                return False
    return True
def rotateMatrix(mat): 
    N = len(mat)
    
    # Consider all squares one by one 
    for x in range(0, int(N / 2)): 
          
        # Consider elements in group    
        # of 4 in current square 
        for y in range(x, N-x-1): 
              
            # store current cell in temp variable 
            temp = mat[x][y] 
  
            # move values from right to top 
            mat[x][y] = mat[y][N-1-x] 
  
            # move values from bottom to right 
            mat[y][N-1-x] = mat[N-1-x][N-1-y] 
  
            # move values from left to bottom 
            mat[N-1-x][N-1-y] = mat[N-1-y][x] 
  
            # assign temp to left 
            mat[N-1-y][x] = temp 

def solution(key, lock):
    M = len(key)
    N = len(lock)
    for i in range(4):
        rotateMatrix(key)
        for curY in range(1-M,N):
            for curX in range(1-M,N):
                lockAnswer = copy.deepcopy(lock)
                flag = True
                for keyCol in range(M):
                    if flag == False:
                        break
                    for keyRow in range(M):
                        curKeyY = curY + keyCol
                        curKeyX = curX + keyRow                        
                        if(curKeyX < 0 or curKeyX >= N or curKeyY < 0 or curKeyY >= N):
                            continue
                        elif (key[keyCol][keyRow] == 0 and lockAnswer[curKeyY][curKeyX] == 1):
                            continue
                        elif (key[keyCol][keyRow] == 1 and lockAnswer[curKeyY][curKeyX] == 0):
                            lockAnswer[curKeyY][curKeyX] = 1
                        else:
                            flag = False
                            break
                if(isSolved(lockAnswer) == True):
                    return True
    return False

def main():
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
    
main()