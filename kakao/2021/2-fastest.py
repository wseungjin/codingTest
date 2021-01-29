from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for courseNum in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order),courseNum)
            temp += comb

        counter = Counter(temp)
        
        if len(counter) !=0 and max(counter.values()) > 1 : 
            for value in counter:
                if max(counter.values()) == counter[value]:
                    answer.append(''.join(value))
    return sorted(answer)

def main():
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2, 3, 5]))
    print(solution(["XYZ", "XWY", "WXA"],[2, 3, 4]))

main()