def solution(baseball):
    answer = 0
    for i in range(1,10):
        for j in range(1,10):
            if(i==j):
                continue
            for k in range(1,10):
                if(i==k):
                    continue
                if(j==k):
                    continue
                flag = True
                newNum=str(i * 100 + j * 10 + k)
                for game in range(len(baseball)):
                    guess=str(baseball[game][0])
                    strike = 0
                    ball = 0
                    for x in range(3):
                        for y in range(3):
                            if(newNum[x]==guess[y]):
                                if(x==y):
                                    strike = strike +1
                                else:
                                    ball = ball + 1
                    if(strike!= baseball[game][1] or ball!= baseball[game][2]):
                        flag = False
                        break
                if flag == True:
                    answer = answer + 1
    
    return answer                

def main():
    baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
    
    print(solution(baseball))
    
main()