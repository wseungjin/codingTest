def solution(A):
    array = []
    for i , v in enumerate(A):
        array.append((v,i))
        
    array.sort()
    
    minIndex = -1
    answer = 0
    for _, i in array:
        if minIndex < i :
            minIndex = i
            answer += 1
            
    return answer

def main():
    print(solution([2,4,1,6,5,9,7]))
    print(solution([4,3,2,6,1]))
    print(solution([2,1,6,4,3,7]))

    
main()
    
