def solution(N=4, stages=[4,4,4,4]):
    speople = []
    fpeople = []
    frate = []
    answer = []
    check = []
    for i in range(0,int(N)):
        speople.append(0)
        fpeople.append(0)
        check.append(0)
        frate.append(0)
    
    
    for stage in range(0,int(N)):
        for people in range(0,len(stages)):
            if(stages[people]>stage+1):
                speople[stage]=speople[stage]+1
            elif(stages[people]==stage+1):
                fpeople[stage]=fpeople[stage]+1

    print(speople)
    print(fpeople)
       
    for i in range(0,int(N)):
        if(speople[i]+fpeople[i]!=0):
            frate[i]=fpeople[i]/(speople[i]+fpeople[i])
            
    print(frate)
        
    for i in range(0,int(N)):
        max=-1
        for j in range(N-1,-1,-1):
            if(check[j]==1):
                continue
            elif(max==-1 and check[j]==0):
                max=j
            elif(frate[max]<=frate[j] and check[j]==0):
                max=j

        check[max]=1
        answer.append(max+1)
        
    print(answer)
    
    return answer

solution()