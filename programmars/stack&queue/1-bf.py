def solution(prices):
    size = len(prices)
    answer = [0] * size
    isFinished = [False] * size
    
    for time in range(size):
        for nowIndex in range(time):
            if prices[time]>=prices[nowIndex] and isFinished[nowIndex] == False:
                answer[nowIndex] += 1
            elif isFinished[nowIndex] == False:
                answer[nowIndex] += 1
                isFinished[nowIndex] = True                 
    return answer

def main():
    
    print(solution([1, 2, 3, 2, 3]))
    print(solution([5, 1, 5, 1, 5]))
    print(solution([1, 2, 3, 4, 5,4,3,2,1,2,3,4,5]))
    print(solution([1, 3, 2, 5,1,8,7,6,2,6,7]))
    print(solution([2,5,1]))
    
main()