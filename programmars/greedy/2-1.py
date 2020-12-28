def getNextIndex(nextIndex,size):
    if nextIndex < 0:
        return size + nextIndex
    if nextIndex >= size:
        return nextIndex - size
    return nextIndex
def solution(name):
    answer = 0
    string= ""
    size = len(name)
    
    for currentIndex in range(size):
        string = string + "A"
    
    currentIndex = 0
    
    while string!= name: 
        
        additionalIndex = 0
        while(1):
            nextIndex1 = getNextIndex(currentIndex + additionalIndex,size)
            nextIndex2 = getNextIndex(currentIndex - additionalIndex,size)
            if string[nextIndex1]!=name[nextIndex1]: 
                answer = answer + additionalIndex
                currentIndex = nextIndex1
                break
            if string[nextIndex2]!=name[nextIndex2]: 
                answer = answer + additionalIndex
                currentIndex = nextIndex2
                break
            additionalIndex = additionalIndex + 1
        if ord(name[currentIndex])<(ord("A")+ord("Z"))/2:
            answer=answer + ord(name[currentIndex])-ord("A")
        else: 
            answer=answer + 1 + ord("Z")-ord(name[currentIndex])
        string = string[:currentIndex] + name[currentIndex] + string[currentIndex+1:]
    return answer


def main():    
    print(solution("AZAAAZ"))
    print(solution("JEROEN"))
    print(solution("JAN"))

    
main()