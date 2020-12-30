from functools import reduce

def getSumDigit(number):
    sumValue = 0
    while number != 0:
        sumValue += number % 10
        number = number // 10
    return sumValue

def solution(A):
    A = sorted(A)
    
    result = {}
    
    for element in A:
        sumValue = getSumDigit(element)
        try:
            result[sumValue].append(element) 
        except:
            result[sumValue] = [element]
    
    maxValue = -1
    sumIndexs = list(result)
        
    for sumIndex in sumIndexs:
        if len(result[sumIndex])>= 2:
            maxValue = max(maxValue,result[sumIndex][-1] + result[sumIndex][-2])
              
    return maxValue
    

def main():
    print(solution([51,71,17,42]))
    print(solution([42,33,60]))
    print(solution([51,32,43]))

    
main()
    
