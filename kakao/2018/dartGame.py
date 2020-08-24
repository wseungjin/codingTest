import re
import math

def solution(dartResult):
    regex = re.compile(r'[\d]+[SDT][#*]?')
    regex1 = re.compile(r'[\d]+')
    regex2 = re.compile(r'[SDT]')
    regex3 = re.compile(r'[#*]')

    array = regex.findall(dartResult)
    score = 3 *[0]
    
    for i,element in enumerate(array):
        num=int(regex1.search(element).group())
        word=regex2.search(element).group()
        specialMatch=regex3.search(element)
        specialWord = ""
        if(specialMatch):
            specialWord = specialMatch.group()
        
        if(word == "S"):
            score[i] = math.pow(num,1)
        elif(word == "D"):
            score[i] = math.pow(num,2)
        elif(word == "T"):
            score[i] = math.pow(num,3)
                        
        if(specialWord == "*"):
            if (i>0):
                score[i-1] = score[i-1] * 2
            score[i] = score[i] * 2
        elif(specialWord == "#"):
            score[i] = score[i] * (-1)
            
    answer = 0
    
    for element in score:
        answer = answer + int(element)
    return answer





dartResult = "10S2D*3T"

print(solution(dartResult))