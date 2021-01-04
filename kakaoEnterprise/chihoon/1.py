def solution(x,spaces):
    
    sortedArray = []
    for index,value in enumerate(spaces):
        sortedArray.append((value,index))

    sortedArray.sort()
    minValues = []
    for start in range(len(spaces) - x + 1):
        for value in sortedArray:
            if start <= value[1] and value[1] < start + x:
                minValues.append(value[0])
                break
            
    return max(minValues)

def main():
    print(solution(2,[8,2,4,6])) 
    print(solution(1,[1,2,3,1,2]))

main()