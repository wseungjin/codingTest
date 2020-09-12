def getElements(orders):
    elements = set()
    
    for order in orders:
        for i in range(len(order)):
            elements.add(order[i])
    answer=list(elements)
    answer=sorted(answer)
    return answer

def get1Num(string):
    answer = 0
    for i in range(len(string)):
        if(string[i]) == "1":
            answer = answer +1
    return answer

def padStart(string,length):
    string = string[2:]
    while(len(string)!=length):
        string = "0" + string
    return string

def toStringFromArray(array):
    newStr = ""
    for char in array:
        newStr = newStr + char
    return newStr

def solution(orders,course):
    answer =[]
    elements = getElements(orders)
    numlen =len(elements)
    bit = ""
    for i in range(numlen):
        bit = bit + "1"
    
    dec = int(bit,2)
    bitArray = []
    for num in range(1,dec+1):
        bitArray.append(padStart(bin(num),numlen))

    possibleArray = []
    for courseNum in course:
        tempArray = []
        for bitElement in bitArray: 
            if get1Num(bitElement) == courseNum:
                tempArray.append(bitElement)
        possibleArray.append(tempArray)
    for index, courseArray in enumerate(possibleArray):         
        nowMax = []      
        max = -1
        for possible in courseArray:
            print(possible)
            newSet = []
            for onebit in range(len(possible)):
                if possible[onebit] == "1" :
                    newSet.append(elements[onebit])
            
            numCount = 0
            for order in orders:
                flag = True
                for newSetChar in newSet:
                    if not(newSetChar in order):
                        flag = False
                        break
                    
                if flag:
                    numCount = numCount + 1
                    
            if(numCount>1):
                if(max == -1):
                    max = numCount
                    nowMax.append(toStringFromArray(newSet))
                elif(numCount>max):
                    max = numCount
                    nowMax = []
                    nowMax.append(toStringFromArray(newSet))
                elif(numCount==max):
                    nowMax.append(toStringFromArray(newSet))
        for nowElement in nowMax:
            answer.append(nowElement)            
    return sorted(answer)

def main():
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2, 3, 5]))
    print(solution(["XYZ", "XWY", "WXA"],[2, 3, 4]))

main()