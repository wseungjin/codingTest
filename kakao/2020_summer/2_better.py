import re

def splitedExpression(expression):
    splitedExpression = re.findall('\d+|[\*\-\+]' ,expression)   
    for index in range(len(splitedExpression)):
        if re.match('[\*\-\+]',splitedExpression[index]) == None:
            splitedExpression[index] = int(splitedExpression[index])  
    return splitedExpression

def mul(expressionArray):
    i=0
    while(1):
        try : 
            if(expressionArray[i]=="*"):
                expressionArray[i-1] = expressionArray[i-1] * expressionArray[i+1]
                expressionArray.pop(i+1)
                expressionArray.pop(i)
                i=i-1
            i=i+1
        except :
            break
    return expressionArray

    
def minus(expressionArray):
    i=0
    while(1):
        try : 
            if(expressionArray[i]=="-"):
                expressionArray[i-1] = expressionArray[i-1] - expressionArray[i+1]
                expressionArray.pop(i+1)
                expressionArray.pop(i)
                i=i-1
            i=i+1
        except :
            break
    return expressionArray
    
def plus(expressionArray):
    i=0
    while(1):
        try : 
            if(expressionArray[i]=="+"):
                expressionArray[i-1] = expressionArray[i-1] + expressionArray[i+1]
                expressionArray.pop(i+1)
                expressionArray.pop(i)
                i=i-1
            i=i+1
        except :
            break
    return expressionArray

def solution(expression):
    expressionArray = splitedExpression(expression)
    values = []
    values.append(abs(mul(minus(plus(list(map(lambda x : x,expressionArray)))))[0]))
    values.append(abs(mul(plus(minus(list(map(lambda x : x,expressionArray)))))[0]))
    values.append(abs(plus(mul(minus(list(map(lambda x : x,expressionArray)))))[0]))
    values.append(abs(plus(minus(mul(list(map(lambda x : x,expressionArray)))))[0]))
    values.append(abs(minus(mul(plus(list(map(lambda x : x,expressionArray)))))[0]))
    values.append(abs(minus(plus(mul(list(map(lambda x : x,expressionArray)))))[0]))
    answer=sorted(values,reverse = True)[0]
    return answer


def main():
    expression = "100-200*300-500+20"
    print(solution(expression))
    
main()