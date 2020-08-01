import json

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
data = user_input.split("/")

dataBase = json.loads(data[0])
targetData = data[1]

def get_summary(data, target_value):
    answer = []

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

    for i in range(2):   
        if(inActiveFlag == True):
            break
        for jsonData in dataBase:
            if(saveParent == jsonData["pk"]):
                if(jsonData["is_active"] == False):
                    inActiveFlag = True
                    break
                else:
                    saveParent = jsonData["parent"]
                    answer.append(jsonData["value"])
           
    answerLength = len(answer)         
    if(answerLength == 0 and inActiveFlag == True):
        print("INACTIVE")
    else:
        for i in range(answerLength-1,-1,-1):
            if i == 0 :
                print(answer[i])    
            else:
                print(answer[i]+">", end = "")    
            
get_summary(dataBase,targetData)