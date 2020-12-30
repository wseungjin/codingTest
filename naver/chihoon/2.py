import copy
from collections import deque

def isSame(A,B):
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

def addNewElement(dq,element):
    if len(dq) == 0 or dq[-1] <= element:
        dq.append(element)
    elif dq[0] >= element:
        dq.appendleft(element)

def solution(A):
    answer = sorted(copy.deepcopy(A))
    count = 0
    dq = deque()
    startIndex = 0 
    for currentIndex in range(len(A)):
        addNewElement(dq,A[currentIndex])
        if isSame(dq,answer[startIndex:currentIndex+1]):
            count += 1
            startIndex = currentIndex + 1
            dq = deque()
    
    return count

def main():
    print(solution([2,4,1,6,5,9,7]))
    print(solution([4,3,2,6,1]))
    print(solution([2,1,6,4,3,7]))

    
main()
    
