from collections import deque

def solution(n, edge):
    graph = {}
    for i in range(n):
        graph[i] = []
    for oneEdge in edge:
        graph[oneEdge[0]-1].append(oneEdge[1]-1) 
        graph[oneEdge[1]-1].append(oneEdge[0]-1)   
        
    visited = [False] * n
    maxDistance = 50000
    distance = [maxDistance] * n 
    
    distance[0] = 0
    visited[0] = True
    
    queue = deque([0])
    
    while queue:
        currentIndex = queue.popleft() 
        for nextIndex in graph[currentIndex]:
            if visited[nextIndex] == False:
                distance[nextIndex] = min(distance[currentIndex] + 1,distance[nextIndex])
                visited[nextIndex] = True
                queue.append(nextIndex)

    maxValue = max(distance)
    answer = 0
    for distanceValue in distance:
        if maxValue == distanceValue:
            answer += 1
    return answer

def main():    
    print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
    
main()