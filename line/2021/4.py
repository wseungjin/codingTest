answer = 0
directionENG = ["동","북","서","남"]
direction = [[0,1],[-1,0],[0,-1],[1,0]]

def printMaze(maze,curY,curX):
    print("")
    for y in range(len(maze)):
        for x in range(len(maze)):
            if (curX == x and curY ==y):
                print("@",end ="")
            else:
                print(maze[y][x],end = "")
                
        print("")

def directionChange(nowDirect,turn):
    newDirection = nowDirect + turn
    if newDirection == 4:
        return 0
    elif newDirection == -1:
        return 3
    else: 
        return newDirection

def leftPosition(nowDirect,y,x):
    nextPosi = list(direction[nowDirect])
    nextPosi[0] = nextPosi[0] + y
    nextPosi[1] = nextPosi[1] + x
    return nextPosi

def isOkay(maze,leftPosition,size):
    if leftPosition[0]>-1 and leftPosition[0]<size and leftPosition[1]>-1 and leftPosition[1]<size:
        if(maze[leftPosition[0]][leftPosition[1]]==1):
            return False
        else :
            return True
    return False

def moving(count,nowDirect, maze, y, x):
    global answer 
    size = len(maze)
    if x == size-1 and y == size-1 : 
        return

    if(isOkay(maze,leftPosition(directionChange(nowDirect,1),y,x),size)):
        curY = leftPosition(directionChange(nowDirect,1),y,x)[0]
        curX = leftPosition(directionChange(nowDirect,1),y,x)[1]
        answer = answer + 1
        newDirection = directionChange(nowDirect,1)
        moving(count+1,newDirection,maze,curY,curX)
    else: 
        newDirection = directionChange(nowDirect,-1)
        moving(count+1,newDirection,maze,y,x)
def solution(maze):
    global answer
    moving(3,0,maze,0,0)
    return answer    

def main():
    print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))

    print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))

    print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))

    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))
    
main()