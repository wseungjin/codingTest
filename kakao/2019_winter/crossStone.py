def solution(stones, k):
    min = stones[0]
    for stone in stones:
        if(min>stone):
            min = stone
    
    for cur in range(len(stones)):
        stones[cur] = stones[cur] - min          
    answer = min
    
    oneCycle = True 
    while(oneCycle):
        cur = -1
        oneCycle = True 
        while cur <len(stones):
            flag = False
            nextPosition = 1
            for plus in range(1,k+1):
                if(cur+plus >= len(stones)):
                    flag = True
                    nextPosition = plus
                    break     
                elif(stones[cur+plus]==0):
                    continue
                else: 
                    stones[cur+plus] = stones[cur+plus] - 1
                    flag = True
                    nextPosition = plus
                    break
            if flag:
                cur = cur + nextPosition
            else: 
                oneCycle = False
                break            
        if oneCycle:
            answer = answer + 1
        
            
                        
    
    return answer

def main():    
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
    
main()