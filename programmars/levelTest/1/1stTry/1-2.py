def solution(n, arr1, arr2):
    map = [[" " for i in range(n)] for j in range(n)]
    answer = [""] * n    

    for i in range(n):
        bi1=bin(arr1[i])
        bi2=bin(arr2[i]) 
        bi1=bi1.replace("0b","")
        bi2=bi2.replace("0b","")
        t=0
        for j in range(len(bi1)-1,-1,-1):
            if(bi1[j]=="1"):
                map[i][n-1-t]="#"    
            t= t + 1
        t=0
        for j in range(len(bi2)-1,-1,-1):
            if(bi2[j]=="1"):
                map[i][n-1-t]="#"
            t= t + 1
    for i in range(n):
        for j in range(n):
            answer[i]=answer[i]+map[i][j]
        
    return answer

def main():
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    
    print(solution(n,arr1,arr2))
    
main()