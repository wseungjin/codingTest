def solution(enter, leave):
    answer = [0] * (len(enter) + 1)
    room = []

    currentLeave = 0
    for currentEnter in enter:
        room.append(currentEnter)

        if len(room) > 1:
            for plusOneIndex in range(len(room)-1):
                answer[room[plusOneIndex]] += 1
            answer[room[len(room)-1]] += len(room)-1

        flag = True
        while flag:
            flag = False
            for index, element in enumerate(room):
                if leave[currentLeave] == element:
                    currentLeave += 1
                    del room[index]
                    flag = True
                    break

    return answer[1:]


def main():
    print(solution([1, 3, 2], [1, 2, 3]))
    print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
    print(solution([3, 2, 1], [2, 1, 3]))
    print(solution([3, 2, 1], [1, 3, 2]))
    print(solution([1, 4, 2, 3], [2, 1, 4, 3]))


main()
