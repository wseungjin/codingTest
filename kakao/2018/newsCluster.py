import re
import math

def getSet(string):
    newSet = []
    for i in range(1,len(string)):
        word = string[i-1:i+1]
        if re.match('[a-z][a-z]',word) != None :
            newSet.append(word) 
    return newSet
       
    
def intersection(setList1,setList2):
    intersectionArray = []
    index = 0
    while index < len(setList1):
        element = setList1[index]
        if element in setList2:
            intersectionArray.append(element)
            setList1.pop(setList1.index(element))
            setList2.pop(setList2.index(element))
        else: 
            index = index + 1
    return len(intersectionArray),len(setList1),len(setList2)    


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    s1 = getSet(str1)
    s2 = getSet(str2)
        
    inter,s1Num,s2Num = intersection(s1,s2)
    union = inter + s1Num + s2Num
        
    if len(s1) == 0 and len(s2) == 0 :
        answer = 65536
    else: 
        answer = math.floor((inter/union) * 65536)
    return answer


def main():
    str1 = "handshake"
    str2 = "shake hands"
    print(solution(str1,str2))
    
main()