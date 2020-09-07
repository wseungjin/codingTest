def solution(record):
    nickname = {}
    
    for oneRecord in record:
        splitedRecord = oneRecord.split(" ")
        if splitedRecord[0] == "Enter":
            nickname[splitedRecord[1]] = splitedRecord[2] 
        elif splitedRecord[0] == "Change":
            nickname[splitedRecord[1]] = splitedRecord[2] 
    
    answer = []
    for oneRecord in record:
        splitedRecord = oneRecord.split(" ")
        if splitedRecord[0] == "Enter":
            answer.append(nickname[splitedRecord[1]]+"님이 들어왔습니다.")
        elif splitedRecord[0] == "Leave":
            answer.append(nickname[splitedRecord[1]]+"님이 나갔습니다.")
    return answer


def main():
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

main()