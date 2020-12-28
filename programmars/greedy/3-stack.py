def solution(numbers, k):
    
    stack = []
    
    for number in numbers:
        
        while stack and stack[-1]<number and k > 0:
            k = k -1
            stack.pop()
        stack.append(number)
        
    if k !=0 :
        stack = stack[:-k]  
    
    return ''.join(stack)


def main():
    
    print(solution("1924",2))
    print(solution("1231234",3))
    print(solution("11111",4))

    
main()