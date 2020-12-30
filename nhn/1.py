def solution(boxA,boxB):
    answer = 0
    
    currentAValue = 0
    currentBValue = 0
    
    currentTimeValue = 1
    for i,e in enumerate(boxA):
        currentAValue += e * currentTimeValue
        currentTimeValue *= 0.9
    
    currentTimeValue = 1 
    for i,e in enumerate(boxB):
        currentBValue += e * currentTimeValue 
        currentTimeValue *= 0.9
    
    currentAIndex = 0 
    currentBIndex = 0
    currentTimeValue = 1
    
    while currentAIndex < len(boxA) and currentBIndex < len(boxB):
        if currentAValue >= currentBValue:
            selectedValue = boxA[currentAIndex] * currentTimeValue
            answer += (selectedValue * 1000)
            currentAValue -= selectedValue
            currentBValue *= 0.9
            currentAIndex += 1
        else :
            selectedValue = boxB[currentBIndex] * currentTimeValue
            answer += (selectedValue * 1000)
            currentBValue -= selectedValue
            currentAValue *= 0.9
            currentBIndex += 1
        currentTimeValue *= 0.9 
            
    if currentAIndex < len(boxA) :
        answer += (currentAValue * 1000)     
    if currentBIndex < len(boxB) :
        answer += (currentBValue * 1000)     
    return answer

def main():
    print(solution([3,20],[8,10]))
    
main()