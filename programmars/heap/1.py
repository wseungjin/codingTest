from queue import PriorityQueue

def solution(scoville, K):
    
    que = PriorityQueue()
    
    for item in scoville: 
        que.put(item)
        
    answer = 0
    notPossible = False
    
    while True:
        firstItem = que.get()
        if firstItem >= K:
            break
        if que.empty():
            notPossible = True
            break
        secondItem = que.get()
        newItem = firstItem + secondItem * 2
        que.put(newItem)
        answer += 1 
    if notPossible :
        return -1
    return answer

def main():    
    print(solution([1, 2, 3, 9, 10, 12],7))
    print(solution([1,1],7))
    
main()