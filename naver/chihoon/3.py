import copy

def getAmplitude(array):
    minValue = 1000000000
    maxValue = 0
    for item in array:
        minValue = min(minValue,item)
        maxValue = max(maxValue,item)
    return maxValue-minValue

def solution(A,K):
    
    minValue = 1000000000
    
    for i in range(len(A)-K+1):
        newArray = copy.deepcopy(A[0:i]) + copy.deepcopy(A[i+K:])
        minValue = min(minValue , getAmplitude(newArray))
    return minValue
def main():
    print(solution([5,3,6,1,3],2))
    print(solution([8,8,4,3],2))
    print(solution([3,5,1,3,9,8],4))
    print(solution([1,1,1],2))
    
main()
    