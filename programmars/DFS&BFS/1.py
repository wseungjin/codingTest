answer = 0

def solution(numbers, target):    
    dfs(0,0,numbers,target)
    return answer


def dfs(count,result,numbers,target):
    global answer
    if (count == len(numbers)):
        if result == target:
            answer = answer + 1
        return
    
    dfs(count+1,result+numbers[count],numbers,target)
    dfs(count+1,result-numbers[count],numbers,target)
    
    

def main():
    numbers = [1, 1, 1, 1, 1]	
    target = 3
    
    print(solution(numbers,target))
    
main()