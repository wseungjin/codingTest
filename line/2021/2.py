from collections import deque

def solution(ball, order):
    answer = []
    d = deque(ball)    
    pending = []
    
    for command in order:
        if command == d[0]:
            answer.append(d.popleft())
        elif command == d[-1]:
            answer.append(d.pop())
        else:
            pending.append(command)
            
        index = 0
        while index < len(pending):
            if d[0] in pending:
                pending.pop(pending.index(d[0]))
                answer.append(d.popleft())
            elif d[-1] in pending:
                pending.pop(pending.index(d[-1]))
                answer.append(d.pop())
            else:
                index = index + 1
        
    return answer

def main():
    print(solution([1, 2, 3, 4, 5, 6],[6, 2, 5, 1, 4, 3]))
    print(solution([11, 2, 9, 13, 24],[9, 2, 13, 24, 11]))

main()