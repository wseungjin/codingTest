from itertools import combinations

def solution(clothes):
    
    answer = 0
    clothes = sorted(clothes,key= lambda x:x[1])
    arrayNum = [1]
    arrayName = clothes[0][1]
    t=0
    for i in range(1,len(clothes)):
        if clothes[i][1]==arrayName:
            arrayNum[t]=arrayNum[t]+1
        else:
            arrayName = clothes[i][1]
            arrayNum.append(1)
            t=t+1
    
    for i in range(1,len(arrayNum)+1):
        comb=list(combinations(arrayNum,i))
        for i in comb:
            result=i[0]
            for j in range(1,len(i)):
                result = result * i[j]
            answer = answer + result
    return answer

def main():
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    
    print(solution(clothes))
    
main()