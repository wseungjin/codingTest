def solution(n, s, a, b, fares):
    s -= 1 
    a -= 1 
    b -= 1
    
    INF = 200 * 100001
    dist = [[INF for i in range(n)] for j in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    for fare in fares:
        dist[fare[0]-1][fare[1]-1] = fare[2]
        dist[fare[1]-1][fare[0]-1] = fare[2]
         
    for mid in range(n):
       for start in range(n):
           for end in range(n):
               if dist[start][end] > dist[start][mid] + dist[mid][end]:
                   dist[start][end] = dist[start][mid] + dist[mid][end]
                   
    answer = INF
    for mid in range(n):
        answer = min(answer,dist[s][mid] + dist[mid][a] + dist[mid][b])    
    return answer

def main():
    print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
    
main()