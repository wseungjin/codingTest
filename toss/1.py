# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
array = user_input.split(" ")

newOrder = ["8","5","2","4","3","7","6","1","0","9"]

answer = []

for i in range(len(newOrder)):
    for j in range(len(array)):
        if (array[j] == newOrder[i]):
            answer.append(newOrder[i])
            
for i in range(len(answer)):
    print(answer[i],end=" ")
