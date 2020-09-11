def get1Num(string):
    answer = 0
    for i in range(len(string)):
        if(string[i]) == "1":
            answer = answer +1
    return answer

def padStart(string,length):
    string = string[2:]
    while(len(string)!=length):
        string = "0" + string
    return string

def same(array1,array2,bit):
    array1Str = ""
    array2Str = ""
    for i in range(len(array1)):
        if(bit[i]=="1"):
            array1Str = array1Str + array1[i] + "/"
            array2Str = array2Str + array2[i] + "/"
    if(array1Str==array2Str):
        return True
    else:
        return False
def solution(relation):
    answer = 0

    numlen =len(relation[0])
    bit = ""
    for i in range(numlen):
        bit = bit + "1"
    
    dec = int(bit,2)
    bitArray = []
    for num in range(1,dec+1):
        bitArray.append(padStart(bin(num),numlen))
        
    bitArray=sorted(bitArray,key = lambda x:get1Num(x))
    # 모든 경우의 수
    successBitArray = []
    # 가능한 경우의 수
    for bit in bitArray:
        flag = True
        for first in range(len(relation)):
            if(flag == False):
                break
            for second in range(first+1,len(relation)):
                if same(relation[first],relation[second],bit) == True:
                    flag = False
                    break
        if flag==True:
            successBitArray.append(bit)
    successArray= [1] * len(successBitArray)
    # 미니멀리티로 한번 더 거름
    for first in range(len(successBitArray)):
        for second in range(first+1,len(successBitArray)):
            if same(successBitArray[first],successBitArray[second],successBitArray[first]) == True:
                successArray[second] = 0
                
    for success in successArray:
        if(success==1):
            answer = answer + 1
    return answer


def main():
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

main()