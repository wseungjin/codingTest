def solution(strings, n):
    strings=sorted(strings)
    strings=sorted(strings,key= lambda x:x[n])

    answer = strings
    return answer

def main():
    strings = ["sun", "bed", "car"]
    n = 1
    
    print(solution(strings,n))
    
main()