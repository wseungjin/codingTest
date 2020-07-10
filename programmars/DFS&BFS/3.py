answer = 100

def solution(begin,target,words):
    global answer
    visited = [False] * len(words)
    route = []
    if target in words:
        dfs(0,begin,target,words,visited,route)
        if answer == 100:
            answer = 0
    else:
        answer = 0
    return answer
            
def dfs(count,begin,target,words,visited,route):
    global answer
    if(count>len(words)):
        return
    if(begin == target):
        answer = min(count,answer)
        return
    
    for i in range(len(words)):
        errorCount = 0
        for j in range(len(words[i])):
            if words[i][j] != begin[j] :
                errorCount = errorCount + 1
        if errorCount == 1:
            if visited[i] == False :
                visited[i] = True
                route.append(words[i])
                dfs(count+1,words[i],target,words,visited,route)
                route.pop()
                visited[i] = False 
    
    
    

def main():
    begin = "hit"
    target	= "cog"
    words =  ["hot", "dot", "dog", "lot", "log", "cog"]
    
    print(solution(begin,target,words))
    
main()