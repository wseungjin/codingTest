def solution(m, n, puddles):
    array=[[0 for i in range(m)] for j in range(n)]
    
    for i in range(len(puddles)):
        array[puddles[i][1]-1][puddles[i][0]-1] = -1
    
    # print(array)
    array[0][0] = 1
    for i in range(1,m):
        if array[0][i]==-1 or array[0][i-1] == -1 or array[0][i-1] == 0 :
            continue
        else:
            array[0][i]= 1
        
    for i in range(1,n):
        if array[i][0]==-1 or array[i-1][0] == -1 or array[i-1][0] == 0 :
            continue
        else:
            array[i][0]= 1
    
    
    # print(array)
        
    for i in range(1,n):
        for j in range(1,m):
            if array[i][j] == -1:
                continue
            elif array[i][j-1] == -1 and array[i-1][j] == -1:
                array[i][j] = 0
            elif array[i][j-1] == -1 or array[i-1][j] == -1 :
                array[i][j] = max(array[i][j-1],array[i-1][j])
            else:
                array[i][j] = (array[i][j-1]+array[i-1][j])%1000000007
    # print(array)
    answer = array[n-1][m-1]
    return answer

def main():
    m = 4
    n = 3
    puddles = [[1,3],[3,1]]
    
    print(solution(m,n,puddles))
    
main()