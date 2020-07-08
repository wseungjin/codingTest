def solution(genres, plays):
    answer = []
    index=[i for i in range(len(genres))]
    newSet=list(zip(genres,plays,index))
    newSet=sorted(newSet,key= lambda x:x[1],reverse = True)
    newSet=sorted(newSet,key= lambda x:x[0])
    genreName= [newSet[0][0]]
    genreNum = [newSet[0][1]]
    t=0
    for i in range(1,len(newSet)):
        if(genreName[t]==newSet[i][0]):
            genreNum[t] = genreNum[t] + newSet[i][1]
        else:
            genreName.append(newSet[i][0])
            genreNum.append(newSet[i][1])
            t= t+1
            
    
    genTuple=list(zip(genreName,genreNum))
    genTuple=sorted(genTuple,key= lambda x:x[1],reverse = True)
    
    
    for i in range(len(genTuple)):
        for j in range(len(newSet)):
            if(genTuple[i][0]==newSet[j][0]):
                answer.append(newSet[j][2])
                if(j+1<len(newSet) and genTuple[i][0]==newSet[j+1][0]):
                    answer.append(newSet[j+1][2])
                break
    
    return answer


def main():
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    
    print(solution(genres,plays))
    
main()