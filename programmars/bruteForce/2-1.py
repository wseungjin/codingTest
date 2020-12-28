import itertools

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



def solution(numbers):
    
    possible = []
    
    for i in range(len(numbers)):
        possibleList = list(map(''.join, itertools.permutations(numbers,i+1)))
        for possibleValue in possibleList:
            possible.append(int(possibleValue))

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