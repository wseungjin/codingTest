def getNextIndex(i,j, length):
    nextIndex = i + j - 1
    if nextIndex >= length:
        nextIndex -= length
    return nextIndex

def setTrue(visited,startIndex,endIndex):
    if endIndex >= len(visited):
        for i in range(startIndex,len(visited)):
            visited[i] = True
        for i in range(0,endIndex - len(visited)):
            visited[i] = True       
    else: 
        for i in range(startIndex,endIndex):
            visited[i] = True
        
def isOK(visited,startIndex,endIndex):
    if endIndex >= len(visited):
        for i in range(startIndex,len(visited)):
            if(visited[i] == True):
                return False
        for i in range(0,endIndex - len(visited)):
            if(visited[i] == True):
                return False     
    else: 
        for i in range(startIndex,endIndex):
            if(visited[i] == True):
                return False
    return True
def solution(n, weak, dist):
    
    dist = sorted(dist)
    
    weakLen = len(weak)
    
    weakDist = []
    
    answer = 0
    
    for i in range(weakLen-1):
        weakDist.append(weak[i+1] - weak[i])
    
    weakDist.append(weak[0] + n - weak[weakLen-1])
    
    sumDist = [[0 for i in range(weakLen)] for j in range(weakLen)]
        
    for i in range(weakLen):
        for j in range(1,weakLen):
            nextIndex = getNextIndex(i,j,weakLen)
            sumDist[i][j] = sumDist[i][j-1] + weakDist[nextIndex]
    
    visited = [False] * weakLen
            
    for length in range(weakLen-1,-1,-1):
        for d in dist:
            for i in range(weakLen):
                if sumDist[i][length] <= d and isOK(visited,i,i+length+1):
                    setTrue(visited,i,i+length+1)
                    answer += 1
                    break
                                     
    for v in visited:
        if v == False:
            return -1
    return answer



def main():
    print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
    print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))
    print(solution(12,[1, 8],[1,1]))


    
main()