def solution(arrangement):
    stack = []
    stack.append(arrangement[0])
    answer = 0
    curBar= 1
    for i in range(1,len(arrangement)):
        if(arrangement[i] == "(") :
            stack.append(arrangement[i])
            curBar = curBar + 1
        elif(arrangement[i-1] == "(" and arrangement[i] == ")"):
            stack.pop()
            curBar = curBar - 1
            answer = answer + curBar
        elif(stack[len(stack)-1] == "(" and arrangement[i] == ")"):
            stack.pop()
            answer = answer + 1
            curBar = curBar - 1
    return answer

def main():
    arrangement = "()(((()())(())()))(())"	
    
    print(solution(arrangement))
    
main()