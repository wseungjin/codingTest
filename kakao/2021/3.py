answer = 0
data = {'java': {'backend': {'junior': {'chicken': {} , "pizza" : {}},"senior": {'chicken': {} , "pizza" : {}}}, "frontend" : {'junior': {'chicken': {} , "pizza" : {}},"senior": {'chicken': {} , "pizza" : {}}}} ,
    'python': {'backend': {'junior': {'chicken': {} , "pizza" : {}},"senior": {'chicken': {} , "pizza" : {}}}, "frontend" : {'junior': {'chicken': {} , "pizza" : {}},"senior": {'chicken': {} , "pizza" : {}}}},
    'cpp': {'backend': {'junior': {'chicken': {} , "pizza" : {}},"senior": {'chicken': {} , "pizza" : {}}}, "frontend" : {'junior': {'chicken': {} , "pizza" : {}},"senior": {'chicken': {} , "pizza" : {}}}}}

def putData(info):
    for oneInfo in info:
        splitedArray = oneInfo.split(" ") 
        cur = data
        for index, splitElement in enumerate(splitedArray):
            if(index == 4):
                if not(splitElement in cur):
                    cur[splitElement] = 1
                else: 
                    cur[splitElement] = cur[splitElement] + 1
            else:
                cur = cur[splitElement]
                
def makeCommand(oneQuery):
    command = oneQuery.split(" and ")
    lastCommand=command.pop()
    command.append(lastCommand.split(" ")[0])
    command.append(lastCommand.split(" ")[1])
    return command

def dfs(count,command,curData):
    global answer
    if count == 4:
        finalValues = list(curData.items())
        for key,value in finalValues:
            if(int(key)>=int(command[4])):
                answer = answer + value
        return
    nowKeys = []
    if command[count] == "-":
        nowKeys = list(curData.keys())
    else:
        nowKeys = [command[count]]
    
    for nowCommand in nowKeys:
        dfs(count+1,command,curData[nowCommand])

def solution(info, query):
    global answer
    totalAnswer = []
    putData(info)
    for oneQuery in query:
        answer = 0
        command = makeCommand(oneQuery)
        dfs(0,command,data)
        totalAnswer.append(answer)
    return totalAnswer

def main():
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
                   ,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
    
main()