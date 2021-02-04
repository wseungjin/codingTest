import bisect

def getData(info):
    
    data = {}
    for oneInfo in info:
        splitedArray = oneInfo.split(" ") 
        lastNum = int(splitedArray.pop())
        
        elements = []
        for i in range(16):
            bits = bin(i)[2:].zfill(4)
            string = ""
            for i in range(4):
                if bits[i] == "1":
                    string += splitedArray[i]
                else: 
                    string += "-"
            
            elements.append(string)
      
        for element in elements:
            try:
                data[element].append(lastNum)
            except:             
                data[element] = [lastNum]
        
    return data

def sortingAll(data):
    for key in data:
        data[key] = sorted(data[key])

def parse(oneQuery):
    splitedArray = oneQuery.split(" and ")
    last=splitedArray.pop()
    lastElement = last.split(" ")[0]
    lastNum = int(last.split(" ")[1])
    splitedArray.append(lastElement)
    string = ''.join(splitedArray)
    return string,lastNum

def binSearch(array,num):
    return len(array) - bisect.bisect_left(array, num)
    
def solution(info, query):
    data = getData(info)
    sortingAll(data)
    answer = []
    for oneQuery in query:
        string, compareNum = parse(oneQuery)
        
        if string in data:
            answer.append(binSearch(data[string],compareNum))
        else:
            answer.append(0)
    return answer

def main():
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
                   ,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
    
main()