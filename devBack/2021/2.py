
def printTable(table):
    for row in table:
        for e in row:
            print(e, end="      ")
        print("")

    print("")
    print("")


def solution(rows, columns, queries):

    table = []
    answer = []

    for y in range(rows):
        row = []
        for x in range(columns):
            row.append(y * columns + x + 1)
        table.append(row)

    for query in queries:
        y1, x1, y2, x2 = query
        y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1

        minValue = 10000

        saveValue1 = table[y1][x2]
        for curX in range(x2, x1, -1):
            table[y1][curX] = table[y1][curX-1]
            if table[y1][curX] < minValue:
                minValue = table[y1][curX]

        saveValue2 = table[y2][x2]
        for curY in range(y2, y1, -1):
            table[curY][x2] = table[curY-1][x2]
            if table[curY][x2] < minValue:
                minValue = table[curY][x2]

        saveValue3 = table[y2][x1]
        for curX in range(x1, x2, 1):
            table[y2][curX] = table[y2][curX + 1]
            if table[y2][curX] < minValue:
                minValue = table[y2][curX]

        saveValue4 = table[y1][x1]
        for curY in range(y1, y2, 1):
            table[curY][x1] = table[curY+1][x1]
            if table[curY][x1] < minValue:
                minValue = table[curY][x1]

        if saveValue1 < minValue:
            minValue = saveValue1

        if saveValue2 < minValue:
            minValue = saveValue2

        if saveValue3 < minValue:
            minValue = saveValue3

        if saveValue4 < minValue:
            minValue = saveValue4

        table[y1 + 1][x2] = saveValue1
        table[y2][x2 - 1] = saveValue2
        table[y2 - 1][x1] = saveValue3
        table[y1][x1 + 1] = saveValue4

        answer.append(minValue)

    return answer


def main():
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]	))

    print(
        solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]	))
    print(solution(100, 97, [[1, 1, 100, 97]]))


main()
