def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j]= triangle[i][j] + triangle[i-1][0]
            elif j == len(triangle[i])-1 :
                triangle[i][j]= triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j]= triangle[i][j] + max(triangle[i-1][j-1],triangle[i-1][j])
    answer = sorted(triangle[len(triangle)-1],reverse = True)
    return answer[0]

def main():
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    
    print(solution(triangle))
    
main()