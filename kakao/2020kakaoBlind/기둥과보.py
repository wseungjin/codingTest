def isOK(n,bo,gidung):
    for x in range(n+1):
        if bo[0][x] == 1:
            return False 
    
    for y in range(1,n+1):
        for x in range(n):
            if gidung[y][x] == 1:
                flag = False
                #  기둥 바로 밑
                if gidung[y - 1][x] == 1:
                    flag = True
                #  왼쪽 끝인데 보 있을때 
                if x == 0 and bo[y][x] == 1:
                    flag = True
                #  오른쪽끝(왼쪽에만 보있을 떄) 
                if x>0 and bo[y][x-1] == 1 :
                    flag = True
                # 왼쪽끝(오른쪽에만 보있을 때) 
                if x>0 and bo[y][x] == 1:
                    flag = True
                if flag == False:
                    return False
                
            if bo[y][x] == 1:
                flag = False
                # 왼쪽에 기둥
                if gidung[y-1][x] == 1:
                    flag = True
                # 오른쪽에 기둥
                if x+1 < n+1 and gidung[y-1][x+1] == 1:
                    flag = True
                # 양쪽끝에 보 
                if x>0 and x+1 < n+1 and bo[y][x-1] == 1 and bo[y][x+1] == 1:
                    flag = True
                if flag == False:
                    return False
    return True

 
    

def solution(n, build_frame):
    
    gidung = [[0 for i in range(n+1)] for j in range(n+1)] 
    bo = [[0 for i in range(n+1)] for j in range(n+1)] 
    
    for command in build_frame:
        x,y,a,b = command[0],command[1],command[2],command[3]
                
        saveGidung = gidung[y][x]
        saveBo = bo[y][x]
        if a == 0:
            if b == 0 and gidung[y][x] == 1:
                gidung[y][x] = 0
            if b == 1:
                gidung[y][x] = 1
        else: 
            if b == 0 and bo[y][x] == 1:
                bo[y][x] = 0
            if b == 1:
                bo[y][x] = 1

        if isOK(n,bo,gidung) == False:
            if a == 0:
                gidung[y][x] = saveGidung
            else: 
                bo[y][x] = saveBo        

    answer = []
    
    for y in range(n+1):
        for x in range(n+1):
            if bo[y][x] == 1:
                answer.append([x,y,1])
            if gidung[y][x] == 1:
                answer.append([x,y,0])
    
    answer = sorted(answer,key=lambda x:x[2])
    answer = sorted(answer,key=lambda x:x[1])
    answer = sorted(answer,key=lambda x:x[0])

    return answer

def main():
    print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))  
    print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))

    
main()