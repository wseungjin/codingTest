def solution(n):
    ans = 0
    while n !=0:
        if n%2 == 0:
            n=int(n/2)
        else:
            n= n- 1
            ans = ans + 1

    return ans
def main():
    n = 5000
    
    print(solution(n))
    
main()