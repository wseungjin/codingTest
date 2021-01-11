import copy

answer = 20

def isDone(weakVisited):
    for v in weakVisited:
        if v == False:
            return False
    return True

def setVisited(n,weakVisited,weak,d,index):
    weakVisited[index] = True
    initValue = weak[index]
    for i in range(index+1,len(weakVisited)):
        if initValue + d >= weak[i]:
            weakVisited[i] = True
        else: 
            return
    for i in range(0, index):
        if initValue + d >= weak[i] + n:
            weakVisited[i] = True
        else:
            return


def dfs(count,n,weak,dist,weakVisited,distVisited):
    global answer
    
    if isDone(weakVisited):
        answer = min(answer,count)
        return 
    
    if count == len(weak):
        return
       
    for j,d in enumerate(dist):
        if distVisited[j] == False:
            for i in range(len(weakVisited)):
                if weakVisited[i] == False:
                    saveVisited = copy.deepcopy(weakVisited)
                    distVisited[j] = True
                    setVisited(n,weakVisited,weak,d,i)
                    dfs(count+1,n,weak,dist,weakVisited,distVisited)
                    distVisited[j] = False
                    weakVisited = saveVisited
        

def solution(n, weak, dist):
    global answer
    answer = 200
    weakVisited = [False] * len(weak)
    distVisited = [False] * len(dist)
    dfs(0,n,weak,dist,weakVisited,distVisited)
    if answer == 20:
        return -1
    return answer

def main():
    print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
    print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))
    print(solution(12,[1, 8],[1,1]))
    print(solution(50,[1],[6]))
    print(solution(200,[0,100],[1,1]))


    
main()