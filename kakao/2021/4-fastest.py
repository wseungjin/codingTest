import heapq 

INF = 200 * 100001

def dijkstra(n,s,graph):

    pq = []
    
    dist = [INF] * n    
    dist[s] = 0
    heapq.heappush(pq,(0,s))
    
    while pq:
        distHere, here = heapq.heappop(pq) 
        if distHere > dist[here]:
            continue
        for there, distThere in graph[here]:
            distThere += distHere
            if distThere < dist[there]:
                heapq.heappush(pq, (distThere, there))
                dist[there] = distThere
    return dist
    
def solution(n, s, a, b, fares):
    s -= 1 
    a -= 1 
    b -= 1   
    
    answer = INF
    graph = [[] for _ in range(n)]
    for fare in fares:
        v1, v2, cost = fare[0]-1,fare[1]-1,fare[2]
        graph[v1].append((v2, cost))
        graph[v2].append((v1, cost))
            
    distFromS = dijkstra(n,s,graph)

    for mid in range(n):
        distFromMid = dijkstra(n,mid,graph)
        answer = min(answer,distFromS[mid] + distFromMid[a] + distFromMid[b])    
    return answer

def main():
    print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
    
main()