def solution(name):
    answer1 = 0
    answer2 = 0
    string1= ""
    string2= ""
    for i in range(len(name)):
        # print(name[i])
        string1 = string1 + "A"
        string2 = string2 + "A"
        
    # print(string1)
    for i in range(len(name)):
        if string1 == name:
            break
        if string1[i]!=name[i]: 
            if ord(name[i])<(ord("A")+ord("Z"))/2:
                answer1=answer1 + ord(name[i])-ord("A")
            else: 
                answer1=answer1 + 1 + ord("Z")-ord(name[i])
            string1 = string1[:i] + name[i] + string1[i+1:]
        if string1 == name:
            break
        answer1 = answer1 + 1


        
    if string2 != name:
        if string2[0]!=name[0]: 
            if ord(name[0])<(ord("A")+ord("Z"))/2:
                answer2=answer2 + ord(name[0])-ord("A")
            else: 
                answer2=answer2 + 1 + ord("Z")-ord(name[0])
            string2 = string2[:0] + name[0] + string2[1:]
        if string2 != name:
            answer2 = answer2 + 1
    for i in range(len(name)-1,0,-1):
        if string2 == name:
            break
        if string2[i]!=name[i]: 
            if ord(name[i])<(ord("A")+ord("Z"))/2:
                answer2=answer2 + ord(name[i])-ord("A")
            else: 
                answer2=answer2 + 1 + ord("Z")-ord(name[i])
            string2 = string2[:i] + name[i] + string2[i+1:]

        if string2 == name:
            break
        answer2 = answer2 + 1
            
    answer=min(answer1,answer2)
    return answer


def main():
    name = "AZAAAZ"
    
    print(solution(name))
    
main()