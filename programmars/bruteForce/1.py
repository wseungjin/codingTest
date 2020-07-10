def solution(answers):
    index = [i for i in range(1,4)]
    correct = [0] * 3
    answer = []
    pattern =[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    for i in range(len(answers)):
        if(answers[i]==pattern[0][i%5]):
            correct[0] = correct[0] + 1
        if(answers[i]==pattern[1][i%8]):
            correct[1] = correct[1] + 1
        if(answers[i]==pattern[2][i%10]):
            correct[2] = correct[2] + 1    
    order=list(zip(index,correct))
    order = sorted(order,key = lambda x:x[1],reverse = True)
    max=order[0][1]
    answer.append(order[0][0])
    for i in range(1,len(order)):
        if max==order[i][1]:
            answer.append(order[i][0])
    return answer

def main():
    answers = [1,3,2,4,2]	
    
    print(solution(answers))
    
main()