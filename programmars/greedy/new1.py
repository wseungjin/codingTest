def solution(n, lost, reserve):
    
    beDeleted = []
    for lostStudent in lost:
        for reserveStudent in reserve:
            if lostStudent == reserveStudent:
                beDeleted.append(lostStudent)
                
    for beDeletedStudent in beDeleted:
        lost.remove(beDeletedStudent)
        reserve.remove(beDeletedStudent)
        
    lost = sorted(lost)
    reserve = sorted(reserve)
        
    answer = n - len(lost)
    nowReserveIndex = 0
                    
    for lostStudent in lost:
        while(nowReserveIndex < len(reserve)):
            if (reserve[nowReserveIndex] > lostStudent + 1):
                break
            if (reserve[nowReserveIndex] == lostStudent - 1 ) or  (reserve[nowReserveIndex] == lostStudent + 1 ):
                answer = answer + 1
                nowReserveIndex = nowReserveIndex + 1
                break 
            nowReserveIndex = nowReserveIndex + 1
    return answer

def main():    
    print(solution(5,[2,4],[1,3,5]))
    print(solution(5,[2,4],[3]))
    print(solution(3,[3],[1]))
    print(solution(2,[1,2],[1]))
    print(solution(5,[1,2,4,5],[2,3,4]))
    print(solution(5,[2,3,4],[3,4,5]))
    print(solution(27,[10,16,19,20,24,26,27],[4,7,8,10,13,14,16,17,18,19,21,22,23,24,25,26,27]))     
    print(solution(10,[1,5,10],[7,9,10]))


    
main()