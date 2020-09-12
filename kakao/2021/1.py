import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    
    # 2
    regex1 = re.compile(r'[a-z0-9/_/.]|[/-]')
    result1 = regex1.findall(new_id)
    
    new_id = ""
    for char in result1:
        new_id = new_id + char
            
    # 3
    new_id = re.sub(r'[/.]+',".",new_id)             

    # 4
    if(len(new_id)>2):
        if(new_id[0] == "."):
            new_id=new_id[1:]
        if(new_id[-1] == "."):
            new_id=new_id[0:len(new_id)-1]
        
    elif len(new_id) == 1 and new_id[0] == "." : 
        new_id = ""
        
    # 5
    if (new_id == ""):
        new_id = "a"
        
    # 6
    while len(new_id)>15:
        new_id=new_id[0:len(new_id)-1]
    
    if(new_id[-1] == "."):
        new_id=new_id[0:len(new_id)-1]
      
    # 7
    while len(new_id)<3:
        new_id = new_id + new_id[-1]
    
    return new_id

def main():
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))
    
main()