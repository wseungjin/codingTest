def solution(s, n):
    answer = ''
    for i in range(len(s)):
        newOrd = s[i]
        if ord(s[i])>64 and ord(s[i])<91 :
            if ord(s[i]) + n >90:
                newOrd = ord(s[i]) + n - 26
            else:   
                newOrd = ord(s[i]) + n
                
            answer = answer + chr(newOrd)
                
        elif ord(s[i])>96 and ord(s[i])<123 :
            if ord(s[i]) + n >122:
                newOrd = ord(s[i]) + n - 26
            else:   
                newOrd = ord(s[i]) + n
            answer = answer + chr(newOrd)

        else:
            answer = answer + newOrd
            
    return answer

def main():
    s="z"
    n = 1
    
    print(solution(s,n))
    
main()