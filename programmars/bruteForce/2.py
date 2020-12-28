def isPrime(n):
    if n < 2: 
        return False 
    if n in (2, 3): 
        return True 
    if n % 2 == 0 or n % 3 == 0:
        return False 
    if n < 9: 
        return True 
    k, l = 5, n**0.5 
    while k <= l: 
        if n % k == 0 or n % (k+2) == 0: 
            return False 
        k += 6 
    return True



def dfs(now,possible,numbers,visited):
    
    done = True
    
    for i in range(len(visited)):
        if visited[i] == False:
            done = False
            
    if done :
        return
    
    for nextIndex in range(len(visited)):
        if visited[nextIndex] == False:
            visited[nextIndex] = True
            possible.append(int(now + numbers[nextIndex]))
            dfs(now + numbers[nextIndex],possible,numbers,visited)
            visited[nextIndex] = False
    
    
def solution(numbers):

    visited = [False] * len(numbers)
    possible = []
    
    dfs('',possible,numbers,visited)    
    
    possible=list(set(possible))
    
    answer = 0
    for possibleValue in possible:
        if isPrime(possibleValue):
            answer += 1
    return answer       

def main():    
    print(solution("17"))
    print(solution("011"))
    
main()