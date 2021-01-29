from itertools import combinations

def getElements(orders):
    elements = set()
    for order in orders:
        for i in range(len(order)):
            elements.add(order[i])
    answer=list(elements)
    answer=sorted(answer)
    return answer

def solution(orders, course):
    elements = getElements(orders)
    
    possibleArray = []
    countArray = []

    for courseNum in course:
        possibleArray.append(list(map(''.join,combinations(elements,courseNum))))
        countArray.append([])
        
    for index,possibles in enumerate(possibleArray):
        for possible in possibles:
            count = 0
            for order in orders:
                flag = True
                for pChar in possible:
                    if (pChar in order) == False:
                        flag = False
                        break
                    
                if(flag == True):
                    count += 1
            if count > 1:
                countArray[index].append((possible,count))
               
               
    answer = []         
    for array in countArray:
        if array:
            newArray = sorted(array, key = lambda x:x[1] ,reverse = True)
            answer.append(newArray[0][0])
            maxValue = newArray[0][1]
            
            for i in range(1,len(newArray)):
                if (maxValue != newArray[i][1]):
                    break
                answer.append(newArray[i][0])
                                    
    answer = sorted(answer)
    return answer

def main():
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2, 3, 5]))
    print(solution(["XYZ", "XWY", "WXA"],[2, 3, 4]))

main()