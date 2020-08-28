def solution(gems):
    N = len(gems)
    saveMin = N
    saveCur = 0
    realGems =list(set(gems))
    flag= 0
    for min in range(len(realGems),N):
        if(flag ==1):
            break
        for curlo in range(N):
            realGems = list(set(gems))
            if(curlo+min>N):
                break
            for x in realGems:
                if(x in gems[curlo:curlo+min]):
                    realGems.remove(x)
            if(len(realGems)==0):
                saveMin = min
                saveCur = curlo
                flag=1
                break
            
    answer = [saveCur+1,saveCur+saveMin]
    return answer

    
    
def main():
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))
    
main()