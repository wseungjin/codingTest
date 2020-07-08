from collections import Counter


def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    count1 = Counter(participant)
    count2 = Counter(completion)

    i = 0
    while i<(len(participant)):
        if count1[participant[i]] != count2[participant[i]]:
            answer = participant[i]
            break
        else:
            i = i + count1[participant[i]] 
        
    return answer


def main():
    participant = ["leo", "kiki", "eden","kiki", "eden"]
    completion = ["eden", "kiki","kiki", "eden"]
    
    print(solution(participant,completion))
    
main()