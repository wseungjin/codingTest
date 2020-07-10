answer = 0

def solution(n, computers):
    graph=[[] for i in range(len(computers))]
    visited = [False] * len(computers)
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if(i!=j and computers[i][j]):
                graph[i].append(j)
    
    dfsFirst(graph,visited)
    return answer


def dfsFirst(graph,visited):
    global answer
    for i in range(len(visited)):
        if visited[i] == False :
            answer = answer + 1
            visited[i] = True
            dfs(i,graph,visited) 
            
def dfs(cur,graph,visited):
    print(cur)
    for i in range(len(graph[cur])):
        if visited[graph[cur][i]] == False :
            print(graph[cur][i])
            visited[graph[cur][i]] = True
            dfs(graph[cur][i],graph,visited) 
    
    
    

def main():
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
    
    print(solution(n,computers))
    
    
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    
    print(solution(n,computers))
    
main()