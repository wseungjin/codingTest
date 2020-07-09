import collections

def solution(citations):
    citations=sorted(citations)
    N = len(citations)
    i = 0
    t = 0
    answer = 0   
    count=collections.Counter(citations)
    countList=list(count.values())

    while i < N :
        for j in range(1,citations[i]+1):
            if (N-i>=j and i+countList[t]<=j):
                if answer<j:
                    answer = j
        i = i + countList[t]
        t= t + 1
    return answer

def main():
    citations = [3, 0, 6, 1, 5]
    
    print(solution(citations))
    
main()