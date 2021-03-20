def solution(table, languages, preference):
    scoreTable = []
    for row in table:
        rowTable = []
        splitedRow = row.split(" ")
        targetJob = splitedRow[0]
        splitedRow = splitedRow[1:]

        for lang in splitedRow:
            rowTable.append(lang)
        scoreTable.append((targetJob, rowTable))

    scoreTable = sorted(scoreTable, key=lambda x: x[0])

    answer = ''
    maxScore = -1
    for scoreRow in scoreTable:
        currentScore = 0
        for index in range(len(languages)):
            for i, element in enumerate(scoreRow[1]):
                if element == languages[index]:
                    score = 5-i
                    currentScore += score * preference[index]
        if currentScore > maxScore:
            maxScore = currentScore
            answer = scoreRow[0]
    return answer


def main():
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"]	, [7, 5, 5]))
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))


main()
