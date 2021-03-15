def solution(priorities, location):
    answer = 0

    while 1:
        current = priorities[0]

        flag = True
        for nextElement in priorities:
            if nextElement > current:
                flag = False
                break

        if flag == True:
            if location == 0:
                break

            priorities.pop(0)
            location -= 1
            answer += 1
        else:
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            last = priorities.pop(0)
            priorities.append(last)

    return answer + 1


def main():
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))


main()
