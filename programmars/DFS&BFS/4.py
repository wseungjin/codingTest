
answer = []
done = False

def solution(tickets):
    global answer
    tickets=sorted(tickets,key = lambda x:x[1])
    tickets=sorted(tickets,key = lambda x:x[0]) 
    # print(tickets)
    visited = [False] * len(tickets)
    route = []
    dfs("start",tickets,visited,route)
    return answer
            
def dfs(now,tickets,visited,route):
    global answer
    global done
    if(done == True):
        return
    # print(route)
    
    flag = True
    for i in range(len(visited)):
        if visited[i]==False:
            flag = False
                    
    if flag == True :
        # print(route)
        for i in range(len(route)):
            answer.append(route[i])
        done = True
        return
    
    for i in range(len(tickets)):
        if visited[i] == False :
            if now == "start"  and tickets[i][0]=="ICN":
                visited[i] = True
                route.append(tickets[i][0])
                route.append(tickets[i][1])
                dfs(tickets[i][1],tickets,visited,route)
                route.pop()
                route.pop()
                visited[i] = False 
            
            elif now == tickets[i][0]:
                visited[i] = True
                route.append(tickets[i][1])
                dfs(tickets[i][1],tickets,visited,route)
                route.pop()
                visited[i] = False 
                
    
    
def main():
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print(solution(tickets))
          
main()