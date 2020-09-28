def solution(blocks):
    piramid = [] 
    for col in range(len(blocks)):
        newRow = []
        for row in range(col+1):        
            if row == blocks[col][0]:
                newRow.append(blocks[col][1])
            else:
                newRow.append("@")
        piramid.append(newRow)
        
    for piramidIndex in range(len(piramid)):
        oneRow = piramid[piramidIndex]
        startIndex = -1
        nowElementNum = len(oneRow)
        for index in range(nowElementNum):
            if type(oneRow[index]) is int:
                startIndex = index
                break
        for forward in range(startIndex+1,nowElementNum):
            oneRow[forward] = piramid[piramidIndex-1][forward-1] - oneRow[forward-1]
        for backward in range(startIndex-1,-1,-1):
            oneRow[backward] = piramid[piramidIndex-1][backward] - oneRow[backward+1]

    answer = []
    
    for oneRow in piramid:
        for oneElement in oneRow:
            answer.append(oneElement)    

    return answer
def main():
    print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
    print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))
    
main()