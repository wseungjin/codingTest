def solution(N, stages):
    frate = [0] * (N+1)
    people = sorted(stages)
    
    totalPeople = len(people)
    nowRemainPeople = len(people)
    curStage = 1
    curFailedPeople = 0
    for index in range(0,totalPeople):
        if curStage == people[index] :
            curFailedPeople = curFailedPeople + 1
        else:
            while(curStage != people[index]) :
                frate[curStage - 1] = curFailedPeople/nowRemainPeople
                nowRemainPeople = nowRemainPeople - curFailedPeople
                curStage = curStage + 1
                curFailedPeople = 0
            curFailedPeople = 1
            
    frate[curStage - 1] = curFailedPeople/nowRemainPeople
    nowRemainPeople = nowRemainPeople - curFailedPeople
    curStage = curStage + 1
    curFailedPeople = 0
    
    frate = frate[0:N] 
    
    stageIndex = []
    for i in range(1,N+1):
        stageIndex.append(i)
        
    sortFailRate = list(zip(frate,stageIndex))
    sortFailRate =sorted(sortFailRate, key = lambda x : x[0] ,reverse = True)
    
    answer = []
    for element in sortFailRate:
        answer.append(element[1])
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
solution(4,[4,4,4,4])