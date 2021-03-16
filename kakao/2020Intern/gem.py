def solution(gems):

    gemSet = set()
    for gem in gems:
        gemSet.add(gem)

    length = len(gemSet)
    answer = []

    gemDict = {}
    minValue = 0
    minKey = gems[0]
    for index, gem in enumerate(gems):
        gemDict[gem] = index

        if gem == minKey:
            minValue = index
            for key in gemDict:
                if gemDict[key] < minValue:
                    minValue = gemDict[key]
                    minKey = key

        if len(gemDict.keys()) == length:
            answer.append([minValue, index])
    answer = sorted(answer, key=lambda x: x[1]-x[0])
    return [answer[0][0] + 1, answer[0][1] + 1]


def main():
    print(solution(["DIA", "RUBY", "RUBY", "DIA",
                    "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
    print(solution(["AA", "AB", "AC", "AA", "AC"]))
    print(solution(["XYZ", "XYZ", "XYZ"]))
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))


main()
