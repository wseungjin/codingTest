import collections

def solution(words, queries):
    answer = []
    
    queriesIndex=[i for i in range(len(queries))] 
    
    queriesOrder = list(zip(queries,queriesIndex))
    
    queriesOrder = sorted(queriesOrder,key = lambda x:x[0])
    queriesOrder = sorted(queriesOrder,key = lambda x:len(x[0]))
    
    words = sorted(words)
    queries = sorted(queries)
    
    words = sorted(words,key = lambda x:len(x))
    queries = sorted(queries,key = lambda x:len(x))
    
    wordsCount=list(collections.Counter(words).items())
    queriesCount=list(collections.Counter(queries).items())
    
    # print(queriesCount)
    
    wCount = []
    qCount = []
    
    wCount.append([len(wordsCount[0][0]),wordsCount[0][1]])
    
    curIndex = 0
    for i in range(1,len(wordsCount)): 
        if(wCount[curIndex][0]==len(wordsCount[i][0])):
            wCount[curIndex][1] = wCount[curIndex][1] + wordsCount[i][1]
            
        else: 
            wCount.append([len(wordsCount[i][0]),wordsCount[i][1]])
            curIndex= curIndex + 1
                    
    qCount.append([len(queriesCount[0][0]),queriesCount[0][1]])
    
    curIndex = 0
    for i in range(1,len(queriesCount)): 
        if(qCount[curIndex][0]==len(queriesCount[i][0])):
            qCount[curIndex][1] = qCount[curIndex][1] + queriesCount[i][1]
            
        else: 
            qCount.append([len(queriesCount[i][0]),queriesCount[i][1]])
            curIndex = curIndex + 1
            
    # print(wCount)
    # print(qCount)
    
    curQ = 0
    curW = 0
    curWCount = 0
    curQCount = 0
    breakFlag = False
    
    while curQ < len(queries):
        # if(curQCount>=len(qCount)):
        #     break
        
        while(qCount[curQCount][0]<wCount[curWCount][0]):            
            if curQ >= len(queries) :
                breakFlag = True
                break
            
            else: 
                for i in range(qCount[curQCount][1]):
                    answer.append(0)
                curQ = curQ + qCount[curQCount][1]
                curQCount = curQCount + 1
        
        if(qCount[curQCount][0]!=wCount[curWCount][0]):
            for i in range(qCount[curQCount][1]):
                answer.append(0)
            curQ = curQ + qCount[curQCount][1]
            curQCount = curQCount + 1
            
        else: 
    
            if breakFlag == True:
                break

            for i in range(curQ,curQ+qCount[curQCount][1]):
                answer.append(0)
                for j in range(curW,curW + wCount[curWCount][1]):
                    flag = True
                    for k in range(qCount[curQCount][0]):
                        if(queries[i][k] != "?" and queries[i][k]!=words[j][k]):
                            flag = False
                            
                    if(flag == True):
                        answer[i] = answer[i] + 1
            
            
            curQ = curQ + qCount[curQCount][1]
            curQCount = curQCount + 1
            
            curW = curW + wCount[curWCount][1]
            curWCount = curWCount + 1
        
    answerOrder=list(zip(queriesOrder,answer))
    answerOrder = sorted(answerOrder,key = lambda x:x[0][1])
    for i in range (len(answerOrder)):
        answer[i]= answerOrder[i][1]
    return answer


def main():
    words = ["frodo"]
    queries = ["?????","?????"]
    
    print(solution(words,queries))
    
main()