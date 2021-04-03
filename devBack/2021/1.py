def solution(lottos, win_nums):

    maxRank = 7
    minRank = 7

    for lotto in lottos:

        if lotto == 0:
            maxRank -= 1
        else:
            if lotto in win_nums:
                maxRank -= 1
                minRank -= 1

    if minRank > 6:
        minRank -= 1

    if maxRank > 6:
        maxRank -= 1
    return [maxRank, minRank]


def main():
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]	))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]		))
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]		))


main()
