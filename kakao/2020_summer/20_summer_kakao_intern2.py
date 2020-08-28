def solution(expression):
    i=0
    stack = []
    expressionList = []

    while(1):
        try : 
            if(expression[i]=="*" or expression[i]=="-" or expression[i]=="+"):
                number=0
                for j in range(len(stack)):
                    now=stack[0] 
                    stack.pop(0)           
                    number = number*10 + now
                expressionList.append(number)   
                expressionList.append(expression[i])
            else: 
                stack.append(int(expression[i]))   
            i=i+1
        except :
            break
        
    number= 0
    for j in range(len(stack)):
        now=stack[0] 
        stack.pop(0)           
        number = number*10 + now
    expressionList.append(number)   
    
    answer = []
    possible = list(expressionList)
    
    # * + -

    i=0
    while(1):
        try : 
            if(possible[i]=="*"):
                possible[i-1] = possible[i-1] * possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
        


    i=0
    while(1):
        try : 
            if(possible[i]=="+"):
                possible[i-1] = possible[i-1] + possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="-"):
                possible[i-1] = possible[i-1] - possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    answer.append(possible[0])
    possible = list(expressionList)

    # * - +
    i=0
    while(1):
        try : 
            if(possible[i]=="*"):
                possible[i-1] = possible[i-1] * possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="-"):
                possible[i-1] = possible[i-1] - possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="+"):
                possible[i-1] = possible[i-1] + possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    answer.append(possible[0])
    possible = list(expressionList)

    # + * -
    i=0
    while(1):
        try : 
            if(possible[i]=="+"):
                possible[i-1] = possible[i-1] + possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="*"):
                possible[i-1] = possible[i-1] * possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="-"):
                possible[i-1] = possible[i-1] - possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    answer.append(possible[0])

    possible = list(expressionList)
    # + - *
    
    i=0
    while(1):
        try : 
            if(possible[i]=="+"):
                possible[i-1] = possible[i-1] + possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="-"):
                possible[i-1] = possible[i-1] - possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="*"):
                possible[i-1] = possible[i-1] * possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    answer.append(possible[0])
 
    possible = list(expressionList)
    # - + *
    i=0
    while(1):
        try : 
            if(possible[i]=="-"):
                possible[i-1] = possible[i-1] - possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="+"):
                possible[i-1] = possible[i-1] + possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    i=0
    while(1):
        try : 
            if(possible[i]=="*"):
                possible[i-1] = possible[i-1] * possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
    answer.append(possible[0])

    possible = list(expressionList)
    # - * +
    i=0
    while(1):
        try : 
            if(possible[i]=="-"):
                possible[i-1] = possible[i-1] - possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1

            i=i+1
        except :
            break

    i=0
    while(1):
        try : 
            if(possible[i]=="*"):
                possible[i-1] = possible[i-1] * possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break

    i=0
    while(1):
        try : 
            if(possible[i]=="+"):
                possible[i-1] = possible[i-1] + possible[i+1]
                possible.pop(i+1)
                possible.pop(i)
                i=i-1
            i=i+1
        except :
            break
        

    answer.append(possible[0])
    
    for k in range(6):
        answer[k] = abs(answer[k]) 
    
    answer = sorted(answer)
    
    return answer[5]
    
    
def main():
    expression = "50*6-3*2"
    print(solution(expression))
    
main()