def solution(n, t, m, timetable):
    tt=[["" for i in range(2)] for j in range(len(timetable))]
    
    arr=[["" for i in range(m)] for j in range(n)]
    
    for i in range(len(timetable)):
        tt[i]=timetable[i].split(":")
        
    tt=sorted(tt,key = lambda x:x[1])
    tt=sorted(tt,key = lambda x:x[0])
    
    busTime = [9,0]  
    answer = ''
    curPeople = 0
    curBus = 0  
    
    lastBusFull = False
    
    while curBus<n: 
        if(len(tt)==0):
            break
        if int(tt[0][0])<busTime[0]:
            arr[curBus][curPeople] = tt[0][0]+":"+tt[0][1]
            curPeople = curPeople + 1
            tt.pop(0)
            if curPeople == m :
                curPeople = 0
                curBus = curBus + 1
                busTime[1] = busTime[1] + t
                if (busTime[1]>=60):
                    busTime[1] = busTime[1] - 60
                    busTime[0] = busTime[0] + 1
                if curBus == n :
                    lastBusFull = True
        elif int(tt[0][0])==busTime[0]:
            if int(tt[0][1])<=busTime[1]:
                arr[curBus][curPeople] = tt[0][0]+":"+tt[0][1]
                curPeople = curPeople + 1
                tt.pop(0)
                if curPeople == m :
                    curPeople = 0
                    curBus = curBus + 1
                    busTime[1] = busTime[1] + t
                    if (busTime[1]>=60):
                        busTime[1] = busTime[1] - 60
                        busTime[0] = busTime[0] + 1   
                    if curBus == n :
                        lastBusFull = True
            else:   
                curPeople = 0
                curBus = curBus + 1
                busTime[1] = busTime[1] + t
                if (busTime[1]>=60):
                    busTime[1] = busTime[1] - 60
                    busTime[0] = busTime[0] + 1    
        else: 
            curPeople = 0
            curBus = curBus + 1
            busTime[1] = busTime[1] + t
            if (busTime[1]>=60):
                busTime[1] = busTime[1] - 60
                busTime[0] = busTime[0] + 1   

    if lastBusFull == True:
        result=arr[n-1][m-1].split(":")
        hour = int(result[0]) 
        minute = int(result[1]) - 1
        if minute<0:
            minute = minute + 60
            hour = hour - 1
        if hour<10:
            hour= "0"+str(hour)
        if minute<10:
            minute= "0"+str(minute)
        answer = str(hour) + ":" + str(minute)
        
    else:
        if curBus==n:
            busTime[1] = busTime[1] - t
            if (busTime[1]<0):
                busTime[1] = busTime[1] + 60
                busTime[0] = busTime[0] - 1  
        if busTime[0]<10:
            busTime[0]= "0"+str(busTime[0])
        if busTime[1]<10:
            busTime[1]= "0"+str(busTime[1])
        answer = str(busTime[0]) + ":" + str(busTime[1])    

    return answer
def main():
    n = 10
    t = 60
    m = 45
    timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    
    print(solution(n,t,m,timetable))
    
main()