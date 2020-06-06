import re

def solution(s):
    
    level = 0
    n = len(s)
        
    regex = re.compile(r"\d")
    mo = regex.search(s)
    if mo != None:
        level = level + 1   
    regex = re.compile(r"[a-z]")
    mo = regex.search(s)
    if mo != None:
        level = level + 1   
    regex = re.compile(r"[A-Z]")
    mo = regex.search(s)
    if mo != None:
        level = level + 1   
    regex = re.compile(r"\W")
    mo = regex.search(s)
    if mo != None:
        level = level + 1   
    if n>9:
        level = level + 1     

    return level

def main():
    user_input = input()
    
    print("LEVEL"+str(solution(user_input)))
main()