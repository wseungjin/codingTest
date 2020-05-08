
import re
from collections import Counter


def solution(s):
    s = Counter(re.findall('\d+', s))
    print(s.items())

    answer = []
    return answer


def main():
    s ="{{2},{2,1},{2,1,3},{2,1,3,4}}"	
    
    print(solution(s))
    
main()