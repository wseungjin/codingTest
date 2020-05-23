def solution(p):
    i = p+1
    flag = 0
    while(1):
        n = [0] * 5
        if(i>9999):
            n[4] = i//10000 
        n[3] = (i-n[4]*10000)//1000   
        n[2] = (i-n[4]*10000-n[3]*1000)//100  
        n[1] = (i-n[4]*10000-n[3]*1000 - n[2]* 100)//10
        n[0] = (i-n[4]*10000-n[3]*1000 - n[2]* 100 - n[1] * 10)//1
        
        if(i < 9999):
            n.pop()
        n.sort()
        if(i > 9999):
            for k in range(4):
                if(n[k]==n[k+1]):
                    flag =0
                    break
                flag = 1
        
        else :
            for k in range(3):
                if(n[k]==n[k+1]):
                    flag =0
                    break
                flag = 1
            
        if(flag==1):
            break
        
        i=i+1 
    
    answer = i
    return answer



def main():
    a = 1987
    print(solution(a))
    
main()