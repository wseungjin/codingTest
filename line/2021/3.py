answerCount = 10000000000
answerValue = 10000000000

def findMin(a,b):
    if a>b:
        return b
    else:
        return a

def isStartZero(stringNum):
    if stringNum[0] == "0":
        return True
    return False

def recur(count,n):
    global answerCount
    global answerValue
    
    if n//10 == 0:
        answerCount = count
        answerValue = n
        return
    
    strLen=len(str(n))
    strN = str(n)

    current = []    
    
    if strLen%2 == 0 : 
        current.append(strLen//2)
        current.append(strLen//2+1)
    else:
        current.append(strLen//2)
        current.append(strLen//2)
        
    while current[0] >-1 or current[1]<strLen:
        minValue = 10000000000
        str1 = ""
        str2 = ""
        
        if current[0] >-1 : 
            str1=strN[:current[0]]
            str2=strN[current[0]:]
        
        
        if(len(str1)!=0 and len(str2)!=0 and (not(isStartZero(str2)))):
            minValue = findMin(int(str1) + int(str2),minValue)
            
        if current[1] <strLen : 
            str1=strN[:current[1]]
            str2=strN[current[1]:]
            
    
        if(len(str1)!=0 and len(str2)!=0 and (not(isStartZero(str2)))):
            minValue = findMin(int(str1) + int(str2),minValue)
        
    
        if minValue !=10000000000:
            recur(count+1,minValue)
            return
        else: 
            current[0] =current[0] - 1
            current[1] =current[1] + 1


def solution(n):
    global answerCount
    global answerValue
        
    recur(0,n)
    answer = [answerCount,answerValue]
    return answer

def main():
    print(solution(73425))    
    print(solution(10007))
    print(solution(9))
main()