import heapq

def solution(scoville, K):
    
    heap = []
    
    for item in scoville:
        heapq.heappush(heap, item) 
        
    answer = 0
    notPossible = False
    
    while True:
        firstItem = heapq.heappop(heap)
        if firstItem >= K:
            break
        if len(heap) ==0 :
            notPossible = True
            break
        secondItem = heapq.heappop(heap)
        newItem = firstItem + secondItem * 2
        heapq.heappush(heap, newItem) 
        answer += 1 
    if notPossible :
        return -1
    return answer

def main():    
    print(solution([1, 2, 3, 9, 10, 12],7))
    print(solution([1,1],7))
    
main()