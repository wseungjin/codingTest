def solution(s):
    min = len(s)
    for count in range(1,len(s)):
        before = s[0:count]
        frequency = 1
        newString = ""
        for index in range(count,len(s),count):
            if before == s[index : index + count]:
                frequency = frequency + 1
            else: 
                if frequency == 1 :
                    newString = newString + before
                else: 
                    newString = newString + str(frequency) + before
                frequency = 1
                before = s[index:index + count]   
        if frequency == 1 :
            newString = newString + before
        else: 
            newString = newString + str(frequency) + before
        if len(newString) < min :
            min = len(newString)
    return min

