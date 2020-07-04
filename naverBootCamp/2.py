import copy

def solution(arrayA,arrayB):
    #space for put the elements
    newArrayA = []
    newArrayB = []
    sumArray = []
    complementArray = []
    intersertArray = []
    
    
    for i in arrayA: 
        if not(i in newArrayA):
            newArrayA.append(i)
            
    for i in arrayB: 
        if not(i in newArrayB):
            newArrayB.append(i)
            
    sumArray = copy.deepcopy(newArrayA)
    for i in arrayB: 
        if not(i in sumArray):
            sumArray.append(i)
    sumArray= sorted(sumArray)
    
    complementArray = copy.deepcopy(newArrayA)
    for i in arrayB: 
        if i in complementArray:
            complementArray.remove(i)
            
    for i in arrayA: 
        for j in arrayB:
            if i==j:
                intersertArray.append(i)
    
    answer = [len(newArrayA), len(newArrayB),len(sumArray),len(complementArray),len(intersertArray)]
    
    return answer

def main():
    arrayA = [2,3,4,3,5] 
    arrayB = [1,6,7]  
    print(solution(arrayA,arrayB))

    
main()