def bs(n,times,left,right):
    if(left>right): 
        return left
    
    mid = (left + right) // 2
    
    sumValue = 0
    for i in range(len(times)):
        sumValue += mid//times[i]
        
    if sumValue >= n:
        return bs(n,times,left,mid-1)
    elif sumValue < n:
        return bs(n,times,mid+1,right)

def solution(n, times):
    maxTimes = n * max(times)
    answer = bs(n,times,1,maxTimes)
    return answer

def main():
    
    print(solution(6,[7,10]))
    print(solution(6,[1,1,1,1,1]))
    
main()