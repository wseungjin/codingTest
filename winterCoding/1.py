def solution(n, delivery):    
    answer = ""
    answerArray = ["?"] * (n+1)
    
    delivery=sorted(delivery,key = lambda x:x[2],reverse=True)
    
    for oneDelivery in delivery:
        if oneDelivery[2] == 1:
            answerArray[oneDelivery[0]] = "O"
            answerArray[oneDelivery[1]] = "O"
        else:
            if answerArray[oneDelivery[0]] == "O":
                answerArray[oneDelivery[1]] = "X"
            elif answerArray[oneDelivery[1]] == "O":
                answerArray[oneDelivery[0]] = "X"
    
    # for oneDelivery in delivery:
    # if oneDelivery[2] == 0:
    #     if answerArray[oneDelivery[0]] == "O":
    #         answerArray[oneDelivery[1]] = "X"
    #     else answerArray[oneDelivery[1]] = "O"
    #         answerArray[oneDelivery[0]] = "X"  
    
    for char in answerArray[1:]:
        answer += char      
    
    return answer

def main():
    print(solution(6,[[1, 3, 1], [3, 5, 0], [5, 4, 0], [2, 5, 0]]))
    print(solution(7,[[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]))

    
main()