def solution(prices):
    size = len(prices)
    answer = [0] * size
    stack = [] 
    stackIndex = []
    
    for index,price in enumerate(prices): 
        while stack and stack[-1] > price :
            nowPrice=stack.pop()  
            nowIndex=stackIndex.pop() 
            answer[nowIndex] = index - nowIndex
                         
        stack.append(price)
        stackIndex.append(index)
        
    while stack:
        nowPrice=stack.pop()  
        nowIndex=stackIndex.pop() 
        answer[nowIndex] = (size-1) - nowIndex
                 
    return answer

def main():
    
    print(solution([1, 2, 3, 2, 3]))
    print(solution([5, 1, 5, 1, 5]))
    print(solution([1, 2, 3, 4, 5,4,3,2,1,2,3,4,5]))
    print(solution([1, 3, 2, 5,1,8,7,6,2,6,7]))
    print(solution([2,5,1]))
    
main()