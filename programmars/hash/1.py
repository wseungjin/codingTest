def solution(participant, completion):
    while len(participant)>1:
        i = participant[0]
        if i in completion:
            completion.remove(i)
            participant.remove(i)
        else : 
            break
    answer = participant[0]
    return answer


def main():
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    
    print(solution(participant,completion))
    
main()