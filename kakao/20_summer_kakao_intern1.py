def solution(numbers, hand):
    phone=[[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
    leftFlag = 0
    curLeft = -1
    curRight = -2

    x= 0
    y= 0
    lx = 0
    ly = 0
    rx = 0
    ry = 0
    
    leftDistance = 0
    rightDistance = 0
    
    answer = ''

    if hand == "left":
        leftFlag=1
        
    for i in range(len(numbers)):
        if(numbers[i]==1 or numbers[i]== 4 or numbers[i]==7):
            curLeft = numbers[i]
            answer= answer +"L"
        elif(numbers[i]==3 or numbers[i]== 6 or numbers[i]==9):
            curRight = numbers[i]
            answer= answer +"R"
        else:
            for column in range(4):
                for row in range(3):
                    if(phone[column][row]==numbers[i]):
                        x = row
                        y = column
            for column in range(4):
                for row in range(3):
                    if(phone[column][row]==curLeft):
                        lx = row
                        ly = column
            for column in range(4):
                for row in range(3):
                    if(phone[column][row]==curRight):
                        rx = row
                        ry = column
            leftDistance = abs(x-lx) + abs(y-ly) 
            rightDistance = abs(x-rx) + abs(y-ry)
            if(leftDistance<rightDistance):
                curLeft = numbers[i]
                answer= answer +"L"
            elif(leftDistance>rightDistance):
                curRight = numbers[i]
                answer= answer +"R"
            else:
                if(leftFlag==1):
                    curLeft = numbers[i]
                    answer= answer +"L"                   
                else:
                    curRight = numbers[i]
                    answer= answer +"R"

    return answer
    
    
def main():
    numbers = [1, 3, 4, 5, 0, 2, 1, 5, 0, 2, 1, 2, 1, 0, 5, 9, 3, 4, 5, 0, 2, 1, 0, 5, 9, 5,1, 3, 4, 5, 0, 2, 1, 0, 5, 9, 5,1, 3, 4, 5, 0, 2, 1, 0, 5, 9, 5]
    hand = "right"
    print(solution(numbers,hand))
    
main()