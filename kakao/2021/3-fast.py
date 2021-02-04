
def getElements(splitedArray):
    
    e1 = []
    e2 = []
    e3 = []
    e4 = []
    
    elements = []
    
    if splitedArray[0] == "cpp":
        e1.append(0) 
    elif splitedArray[0] == "java":
        e1.append(8) 
    elif splitedArray[0] == "python":
        e1.append(16) 
    else:
        e1.append(0) 
        e1.append(8) 
        e1.append(16) 
        
    if splitedArray[1] == "backend":
        e2.append(0) 
    elif splitedArray[1] == "frontend":
        e2.append(4)
    else:
        e2.append(0)
        e2.append(4)
            
    if splitedArray[2] == "junior":
        e3.append(0)
    elif splitedArray[2] == "senior":
        e3.append(2)
    else:
        e3.append(0)
        e3.append(2)
        
    if splitedArray[3] == "chicken":
        e4.append(0)
    elif splitedArray[3] == "pizza":
        e4.append(1)
    else: 
        e4.append(0)
        e4.append(1)
        
    for e1e in e1:
        for e2e in e2:
            for e3e in e3:
                for e4e in e4:
                    elements.append(e1e + e2e + e3e + e4e)
    return elements

def getData(info):
    
    data = [[] for i in range(24)]
    for oneInfo in info:
        splitedArray = oneInfo.split(" ") 
        elements = getElements(splitedArray)
        data[elements[0]].append(int(splitedArray[4]))
        
    for i in range(len(data)):
        data[i] = sorted(data[i])
    return data

def search(scores, num):
    size = len(scores)
    return size - bisect.bisect_left(scores, num, lo=0, hi=size)

def parse(oneQuery):
    splitedArray = oneQuery.split(" and ")
    last=splitedArray.pop()
    lastElement = last.split(" ")[0]
    lastNum = int(last.split(" ")[1])
    splitedArray.append(lastElement)

    elements = getElements(splitedArray)
    return elements,lastNum
            
def solution(info, query):
    data = getData(info)
    answer = []
    for oneQuery in query:
        count = 0
        elements, compareNum = parse(oneQuery)
        for element in elements:
            for d in data[element]:
                if d >= compareNum:
                    count += 1 
        answer.append(count)
    return answer

def main():
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
                   ,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
    
main()