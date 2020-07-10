def solution(words, queries):
    answer = []
    
    for i in range(len(queries)) : 
        answer.append(0)
        for j in range(len(words)) :
            if len(queries[i]) == len(words[j]):
                flag = True 
                for k in range(len(queries[i])):   
                    if(queries[i][k] != "?" and queries[i][k]!=words[j][k]):
                        flag = False
                if(flag == True):
                    answer[i] = answer [i] + 1 
                        
    return answer


def main():
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    
    print(solution(words,queries))
    
main()