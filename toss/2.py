import json

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
data = user_input.split("/")

dataBase = json.loads(data[0])
targetData = data[1]

def get_summary(data, target_value):
    answer = []
    answerString = ""
    saveParent = None

    inActiveFlag = False

    for jsonData in dataBase:
        if(targetData == jsonData["value"]):
            if(jsonData["is_active"] == False):
                inActiveFlag = True
                break
            else:
                saveParent = jsonData["parent"]
                answer.append(jsonData["value"])

    count = 0 
    while saveParent: 
        if(inActiveFlag == True):
            break
        for jsonData in dataBase:
            if(saveParent == jsonData["pk"]):
                if(jsonData["is_active"] == False):
                    inActiveFlag = True
                    break
                else:
                    if count < 2:
                        answer.append(jsonData["value"])
                    saveParent = jsonData["parent"]
                    count = count + 1
                    
    if(inActiveFlag == True):
        answerString = "INACTIVE"
    else:
        answerLength = len(answer)
        for i in range(answerLength-1,-1,-1):
            if i == 0 :
                answerString = answerString + answer[i]    
            else:
                answerString = answerString + answer[i]+">"    
                
    return answerString
            
print(get_summary(dataBase,targetData))