import copy 

#1초동안 움직일 수 있는 모든 경우
def move(cur,board):
	move = [(1,0), (0,1), (-1,0), (0,-1)]
	ret=[]
	#이동
	for m in move:
		if board[cur[0]+m[0]][cur[1]+m[1]]==0 and board[cur[2]+m[0]][cur[3]+m[1]]==0:
			ret.append((cur[0]+m[0],cur[1]+m[1],cur[2]+m[0],cur[3]+m[1]))
	
	rotate=[1,-1]
	#가로회전
	if cur[0]==cur[2]:
		for r in rotate:
			if board[cur[0]+r][cur[1]]==0 and board[cur[2]+r][cur[3]]==0:
				ret.append((cur[0]+r,cur[1],cur[0],cur[1]))
				ret.append((cur[2]+r,cur[3],cur[2],cur[3]))
	#세로회전
	else:
		for r in rotate:
			if board[cur[0]][cur[1]+r]==0 and board[cur[2]][cur[3]+r]==0:
				ret.append((cur[0],cur[1],cur[0],cur[1]+r))
				ret.append((cur[2],cur[3],cur[2],cur[3]+r))
	return ret


def solution(board):
    
    n = len(board)
    size = len(board)
    newBoard = [[1 for i in range(n+2)] for i in range(n+2)]
    for i in range(n):
	    for j in range(n):
		    newBoard[i+1][j+1] = board[i][j]
        
    visited = []
    queue = []
    start = (1,1,1,2) 
    
    visited.append(start)    
    queue.append(start)
    curCount = 0

    while queue:
        nextQueue = copy.deepcopy(queue)
        queue = []
        while nextQueue:
            cur = nextQueue.pop(0)  
            if (cur[0] == n and cur[1] == n) or (cur[2] == n and cur[3] == n):
                return curCount
            possibles = move(cur,newBoard)
            for possible in possibles:
                if possible not in visited:
                    queue.append(possible)
                    visited.append(possible) 
                
        curCount += 1

        
    return 0   
def main():
    print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
    
main()