def solution(enter, leave):
    answer = [0] * (len(enter) + 1)
    room = []

    currentEnter = 0

    for currentLeave in leave:

        flag = True
        for index, element in enumerate(room):
            if currentLeave == element:
                del room[index]
                flag = False
                break

        if flag == False:
            continue

        appendNum = 0
        for currentEnterIndex in range(currentEnter, len(enter)):
            room.append(enter[currentEnterIndex])
            currentEnter += 1
            appendNum += 1
            if enter[currentEnterIndex] == currentLeave:
                break

        if appendNum > 0 and len(room) > 1:
            for roomIndex in range(len(room)-appendNum):
                answer[room[roomIndex]] += appendNum
            for roomIndex in range(len(room)-appendNum, len(room)):
                answer[room[roomIndex]] += len(room) - 1

        for index, element in enumerate(room):
            if currentLeave == element:
                del room[index]
                flag = False
                break
    return answer[1:]


def main():
    print(solution([1, 3, 2], [1, 2, 3]))
    print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
    print(solution([3, 2, 1], [2, 1, 3]))
    print(solution([3, 2, 1], [1, 3, 2]))
    print(solution([1, 4, 2, 3], [2, 1, 4, 3]))


main()
