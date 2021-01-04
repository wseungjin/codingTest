def solution(A,K):
    array = []
    for i , v in enumerate(A):
        array.append((v,i))
        
    array.sort()
    
    minAmp = 123456789
    
    for i in range(len(A) - K + 1):
        startIndex = i
        endIndex = i + k - 1
        
        minIndex = 0
        maxIndex = len(array) - 1
        
        while array[minIndex][1] >= startIndex and array[minIndex][1] <= endIndex:
            minIndex += 1
            
        while array[maxIndex][1] >= startIndex and array[maxIndex][1] <= endIndex:
            maxIndex += 1
            
        amp = array[maxIndex][0] - array[minIndex][0]
        
        if amp < minAmp:
            minAmp = amp
            
    return minAmp

def main():
    print(solution([5,3,6,1,3],2))
    print(solution([8,8,4,3],2))
    print(solution([3,5,1,3,9,8],4))
    print(solution([1,1,1],2))

    
main()
    
