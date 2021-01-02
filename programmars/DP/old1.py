def solution(N):
    fib = [0] * 81
    fib[0]=1
    fib[1]=1
    
    for i in range(2,81):
        fib[i]= fib[i-1] + fib[i-2]
    
    if N == 1 :
        answer = 4
    elif N == 2:
        answer = 8
        
    answer = 2 * (fib[N-1] + fib[N-2]) + 2 * fib[N-1]
    return answer

def main():
    N = 5
    
    print(solution(N))
    
main()