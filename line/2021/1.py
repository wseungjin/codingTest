from collections import Counter
import re

def solution(boxes):
    answer = 0

    totalList = []
    for box in boxes:
        for element in box:
            totalList.append(element)
    
    count = Counter(totalList)
    answerList=list(count.items())
    
    for element in answerList:
        if(element[1]%2==1):
            answer = answer + 1
    
    return answer//2

def main():
    print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
    print(solution([[1, 2], [3, 4], [5, 6]]	))
    print(solution([[1, 2], [2, 3], [3, 1]]	))
    
main()