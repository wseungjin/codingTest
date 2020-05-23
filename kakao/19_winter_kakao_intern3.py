def solution(user_id, banned_id):
    bNum = len(banned_id)
    uNum = len(user_id) 
    match = True
    
    two_d_list = []
    for i in range(uNum):
        line = []
        two_d_list.append(line)
    
    print(two_d_list)
    
    for i in range(uNum):
        for j in range(bNum):
            if(len(user_id[i])==len(banned_id[j])):
                for a in range(len(user_id[i])):
                    match=True
                    if(user_id[i][a]!=banned_id[j][a] and banned_id[j][a] !="*"):  
                        match =False  
                        break
                    
                if(match==True) : 
                    two_d_list[i].append(j)
                    
    memory = []
    for i in range(uNum):
        line = []
        two_d_list.append(line)
    
    while(1):
        memory = [-1] * uNum
        myBox = [i for i in range(bNum) ]
        for i in range(uNum):
            for j in range(bNum):
                if(myBox[j] in two_d_list[i]):
                    
                    
    answer = 0
    return answer


def main():
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(solution(user_id,banned_id))
    
main()