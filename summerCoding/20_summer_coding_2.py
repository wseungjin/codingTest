def cal(p,c,a):
    p = p * 3
    c = c * 2
    a.append(p)
    
    return p,c


def solution(n):
    answer = [0,1]
    p = 1 
    c = 1 
    for i in range(2,n+1):
        if(i==c *2):
            p,c= cal(p,c,answer)
        else: 
            answer.append(answer[c]+answer[i-c])        
            
    return answer[n]

def main():
    a = 11
    print(solution(a))
    
main()