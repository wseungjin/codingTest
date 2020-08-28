def reverse(string):
    resultStr = ""
    for char in string:
        if char == "(": 
            resultStr = resultStr + ")"
        elif char == ")": 
            resultStr = resultStr + "("
    return resultStr

def isRight(u):
    stack = []    
    for i in range(len(u)):
        if u[i] == "(" :
            stack.append("(")
        elif u[i] == ")" :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()
    return True

def divide(string):
    stack = []    
    index = 0
    stack.append(string[0])
    for i in range(1,len(string)):
        if len(stack) == 0 :
            index = i
            break 
        if string[i] == "("  and stack[-1] == "(" :
            stack.append("(")
        elif string[i] == "("  and stack[-1] == ")" :
            stack.pop()
        elif string[i] == ")"  and stack[-1] == ")" :
            stack.append(")")
        elif string[i] == ")"  and stack[-1] == "(" :
            stack.pop()   
            
    if index == 0 and len(stack) == 0 :
        index = len(string)
                        
    u = string[:index]
    v = string[index:]
    return u,v
    

def recursive(string):
    if string == "":
        return string
    u,v = divide(string)
    if isRight(u):
        return u + recursive(v)
    else :
        u = u[1:]
        u = u[:len(u)-1]
        return "(" + recursive(v) + ")" + reverse(u)

def solution(p):
    return recursive(p)

print(solution("()))((()"))