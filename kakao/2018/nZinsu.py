def conversion(num):
    if num == 0:
        return "0" 
    elif(num<10):
        return str(num)
    elif num==10:
        return "A"
    elif num==11:
        return "B"
    elif num==12:
        return "C"
    elif num==13:
        return "D"
    elif num==14:
        return "E"
    elif num==15:
        return "F"
    


def nZinsu(n,decimalNum):
    answer = ""
    if(decimalNum == 0):
        answer = "0"
    while(decimalNum>0):
        answer = conversion(decimalNum%n) + answer 
        decimalNum = decimalNum // n
    return answer

def solution(n, t, m, p):
    answer = ''
    totalcount = 0
    decimalNum = 0
    while(totalcount < (t-1)*m+p):
        nZinsuString = nZinsu(n,decimalNum)
        for i in range(len(nZinsuString)):
            if(totalcount >= (t-1)*m+p):
                break
            if(((totalcount)%m)== (p - 1)) :
                answer = answer + nZinsuString[i]                 
            totalcount = totalcount + 1
        decimalNum = decimalNum + 1        
    return answer
    

def main():
    print(solution(2,4,2,1))
    print(solution(16,16,2,1))
    print(solution(16,16,2,2))

main()