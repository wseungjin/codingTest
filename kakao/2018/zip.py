def init(dictionary):
    numA = ord("A")
    for i in range(26):
        dictionary.append(chr(numA+i))




def solution(msg):
    dictionary = []
    init(dictionary)
    answer = []
    
    current = 0
    count = 1
    while current < len(msg):
        if current + count >= len(msg):
            nowInput = msg[current:current+count]
            current = current + count
            count = 1
            answer.append(dictionary.index(nowInput)+1)
        else:
            
            nowInput = msg[current:current+count]
            nextInput = msg[current+count:current+count+1]
            sumInput = nowInput + nextInput
            if sumInput in dictionary:
                count = count + 1
            else:
                current = current + count
                count = 1
                answer.append(dictionary.index(nowInput)+1)
                dictionary.append(sumInput)
        
            
        
    return answer

def main():
    print(solution("KAKAO"))
    print(solution("TOBEORNOTTOBEORTOBEORNOT"))
    print(solution("ABABABABABABABAB"))

main()