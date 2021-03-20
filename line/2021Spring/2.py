from collections import Counter
import re

regex = re.compile(r'[a-zA-Z\d~!@#$%^&*]')

regex1 = re.compile(r'[A-Z]')
regex2 = re.compile(r"[a-z]")
regex3 = re.compile(r'[\d]')
regex4 = re.compile(r'[~!@#$%^&*]')


def is1(string):
    if len(string) > 15 or len(string) < 8:
        return False
    return True


def is2(string):
    result = regex.findall(string)
    if len(result) != len(string):
        return False
    return True


def is3(string):
    possible = 0

    result1 = regex1.search(string)
    if result1 != None:
        possible += 1

    result2 = regex2.search(string)
    if result2 != None:
        possible += 1

    result3 = regex3.search(string)
    if result3 != None:
        possible += 1

    result4 = regex4.search(string)
    if result4 != None:
        possible += 1

    if possible < 3:
        return False
    return True


def is4(string):
    previous = string[0]
    currentCount = 1

    for i in range(1, len(string)):
        if(previous == string[i]):
            currentCount += 1
        else:
            previous = string[i]
            currentCount = 1

        if currentCount >= 4:
            return False
    return True


def is5(string):
    counter = Counter(string)
    if counter.most_common(1)[0][1] >= 5:
        return False
    return True


def is1(string):
    if len(string) > 15 or len(string) < 8:
        return False
    return True


def solution(inp_str):
    answer = []

    if not is1(inp_str):
        answer.append(1)

    if not is2(inp_str):
        answer.append(2)

    if not is3(inp_str):
        answer.append(3)

    if not is4(inp_str):
        answer.append(4)

    if not is5(inp_str):
        answer.append(5)

    if len(answer) == 0:
        answer.append(0)

    return answer


def main():
    print(solution("AaTa+!12-3"))
    print(solution("aaaaZZZZ)"))
    print(solution("CaCbCgCdC888834A"))
    print(solution("UUUUU"))
    print(solution("ZzZz9Z824"))
    print(solution("111234abcd!!"))


main()
