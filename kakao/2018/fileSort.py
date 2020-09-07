import re

def solution(files):
    regex = re.compile(r'[a-zA-Z\-\.\s]+[\d]{1,5}')
    regex1 = re.compile(r'[a-zA-Z\-\.\s]+')
    regex2 = re.compile(r'[\d]{1,5}')
    data = []
    for index,file in enumerate(files): 
        splitedFile = regex.findall(file)[0]
        head = regex1.findall(splitedFile)[0].lower()
        num = regex2.findall(splitedFile)[0]
        data.append([head,int(num),index])

    data=sorted(data,key = lambda x:x[1])
    data=sorted(data,key = lambda x:x[0])
    answer = []
    
    for oneData in data:
        answer.append(files[oneData[2]])
    return answer


def main():
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

main()