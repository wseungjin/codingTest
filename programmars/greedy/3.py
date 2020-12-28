def solution(numbers, k):
    
    size = len(numbers)
    currentSize = len(numbers)
    while currentSize != (size - k):
        for index in range(currentSize):
            if index + 1 == currentSize:
                break
            if int(numbers[index]) < int(numbers[index + 1]):
                numbers = numbers[:index] + numbers[index+1:]
                break
        if currentSize == len(numbers):
            numbers = numbers[:currentSize-1]
        currentSize = len(numbers)
    return numbers


def main():
    
    print(solution("1924",2))
    print(solution("1231234",3))
    print(solution("4177252841",4))

    
main()