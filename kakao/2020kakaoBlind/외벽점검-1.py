from itertools import permutations

def solution(n, weak, dist):
    weakLen = len(weak)
    for i in range(weakLen):
        weak.append(weak[i] + n)
        
    answer = len(dist) + 1
    
    candidates = list(permutations(dist,len(dist)))
    
    for i in range(weakLen):
        
        curWeakWall = weak[i:i+weakLen]
        for candidate in candidates:
                        
            friendIndex , friendCount = 0,1
            possibleCheckLength = curWeakWall[0] + candidate[0]
            
            for index in range(1,weakLen):                
                if possibleCheckLength < curWeakWall[index]:
                    friendCount += 1
                    if friendCount> len(candidate):
                        break
                    friendIndex += 1
                    possibleCheckLength = curWeakWall[index] + candidate[friendIndex]
                    
            answer = min(answer,friendCount)

    if answer > len(dist):
        return -1
    return answer
def main():
    print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
    print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))
    print(solution(12,[1, 8],[1,1]))
    print(solution(50,[1],[6]))
    print(solution(200,[0,5,100],[1,1]))


    
main()