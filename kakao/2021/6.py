min = 1000000

def targetFromCS(x,y,target):
    return 1

def dfs(x,y,index,targets,route,firstFlag,visited,curNum):
    global min    
    
    # print(route)
    # print(firstFlag)
    # print(visited)
    
    curNum= curNum +targetFromCS(x,y,targets[index])
    
    flag = True
    for visitedElement in visited:
        if(visitedElement == False):
            flag = False
            break
    if flag == True :
        if (curNum < min):
            min = curNum 

        return
    
    if firstFlag == True :
        if index%2 == 0:
            visited[index+1] = True
            route.append(index+1)
            dfs(targets[index][0],targets[index][1],index+1,targets,route,False,visited,curNum)
        else:
            visited[index-1] = True
            route.append(index-1)
            dfs(targets[index][0],targets[index][1],index-1,targets,route,False,visited,curNum)        
    else :
        for nextIndex in range(len(visited)):
            if(visited[nextIndex] == False):
                visited[nextIndex] = True
                route.append(nextIndex)
                dfs(targets[index][0],targets[index][1],nextIndex,targets,route,True,visited,curNum)
                route.pop()
                visited[nextIndex] = False

    
    
        
def getinfo(board):    
    target = []    
    for y in range(4):
        for x in range(4):
            if(board[y][x]!=0):
                target.append((x,y))
    return target
    


def solution(board, r, c):
    global min
    targets = getinfo(board)
    for index, target in enumerate(targets):
        answer = 0
        firstFlag = True  
        route = []     
        visited = [False] * len(targets)
        visited[index] = True
        route.append(index)
        dfs(c,r,index,targets,route,firstFlag,visited,0)
        print(min)
    return min + len(targets)


def main():
    solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)
    
main()