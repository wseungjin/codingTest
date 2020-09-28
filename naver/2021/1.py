def solution(m,k):
    kCount = 0
    answer = ""
    for index in range(len(m)):
        if kCount >= len(k):
            answer = answer + m[index:]
            break
        elif m[index] == k[kCount]:
            kCount = kCount + 1
        else :
            answer = answer + m[index]
    return answer
    

def main():
    print(solution("kkaxbycyz","abc"))
    print(solution("acbbcdc","abc"))
    
main()
    
