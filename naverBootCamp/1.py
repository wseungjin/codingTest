def solution(name_list):
    
    answer = False
    
    for i in name_list:
        if(answer==True):
            break
        for j in name_list:
            if i.find(j) != -1 and i!=j:
                answer = True
                break    
    return answer


def main():
    name_list=["가을", "우주", "너굴"]
    
    print(solution(name_list))
    
main()