def solution(n, results):
    
    graph = [[0 for i in range(n)] for j in range(n)]
    
    for result in results:
        graph[result[0]-1][result[1]-1] = 1
        graph[result[1]-1][result[0]-1] = -1
        
    for k in range(n):
        for start in range(n):
            for end in range(n):
                if(graph[start][k] == graph[k][end] and graph[start][end] == 0):
                    graph[start][end] = graph[start][k]
        
    answer = 0
    countFlag = True
    for currentNode,graphElement in enumerate(graph):
        for index,value in enumerate(graphElement):
            if currentNode !=index and value == 0:
                countFlag = False
                break
        if countFlag:
            answer += 1         
        countFlag = True
        
    return answer

def main():    
    print(solution(3,[[1,3],[2,3],[1,2]]))
    print(solution(5,[[4, 3], [3, 2], [1, 2], [2, 5]]))
    print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
    print(solution(5,[[1, 2], [2, 3], [3, 4], [4, 5]]))
    print(solution(4,[[1, 2], [3, 4]]))

main()