def solution(numbers):
    
    newNumbers=[""] * len(numbers)
    index=[i for i in range(len(numbers))]
    for i in range(len(numbers)):
        numbers[i]=str(numbers[i])
        strLength = len(numbers[i])
        if strLength == 1 :
            for j in range (0,12,strLength):
                newNumbers[i] = newNumbers[i] + numbers[i]
        elif strLength == 2 :
            for j in range (0,12,strLength):
                newNumbers[i] = newNumbers[i] + numbers[i]
        elif strLength == 3 : 
            for j in range (0,12,strLength):
                newNumbers[i] = newNumbers[i] + numbers[i]
        elif strLength == 4 : 
            for j in range (0,12,strLength):
                newNumbers[i] = newNumbers[i] + numbers[i]
    newTuple=list(zip(newNumbers,index))
    newTuple=sorted(newTuple,key= lambda x:x[0],reverse=True)
    answer = ''
    for i in range(len(numbers)):
        if(answer=='0' and numbers[newTuple[i][1]]=='0'):
            answer='0'
        else:
            answer=answer+numbers[newTuple[i][1]]
    return answer

def main():
    numbers = [0, 0, 0, 0, 0]
    
    print(solution(numbers))
    
main()