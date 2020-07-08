def solution(phone_book):
    phone_book=sorted(phone_book)
    length = len(phone_book)
    answer = True
    for i in range (length):
        if answer == False:
            break
        for j in range(i+1,length):
            findValue = phone_book[j].find(phone_book[i],0,len(phone_book[i]))
            if findValue == -1:
                break
            else: 
                answer = False
                break
    
    return answer

def main():
    phone_book = ["123", "456", "789"]
    
    print(solution(phone_book))
    
main()