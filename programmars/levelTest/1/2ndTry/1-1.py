from math import gcd

def lcm(x,y):
    return x * y // gcd(x,y)

def solution(n, m):
    answer = []
    
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    
    return answer

def main():
    n = 3
    m = 12
    
    print(solution(n,m))
    
main()