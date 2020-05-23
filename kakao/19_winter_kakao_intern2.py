
import re
from collections import Counter


def solution(s):
    s = Counter(re.findall('\d+', s))
    answer=list(map(int,[k for k, v in sorted(s.items(),key = lambda x : x[1],reverse=True)]))
    return answer


def main():
    s ="{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))
    
main()