def solution(n, times):
    high = n * max(times)
    low = 1
    mid = (high + low)//2
    times = sorted(times)
    sumValue = 0
    
    
    while low <= high:
        
        for time in times:
            sumValue += mid//time
        
        if sumValue >= n:
            high = mid - 1
        elif sumValue < n:
            low = mid + 1
            
        sumValue = 0
        mid = (high + low)//2
        
    return low

def main():
    
    print(solution(6,[7,10]))
    print(solution(6,[1,1,1,1,1]))
    
main()