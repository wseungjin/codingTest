def solution(stones, k):
    stoneSet = set()

    for stone in stones:
        stoneSet.add(stone)

    minList = list(stoneSet)
    minList = sorted(minList)
    stones.append(200000001)

    for index, current in enumerate(minList):
        length = 0
        for stone in stones:
            if length >= k:
                return minList[index-1]
            if current > stone:
                length += 1
            else:
                length = 0
    return minList[len(minList)-1]


def main():
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


main()
