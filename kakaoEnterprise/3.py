def solution():
    
    answer =0
    
    # inf = open('input.txt');

    # n = inf.readline();
    n = input()
    
    n, k = n.split(" ")    
    n, k = int(n), int(k)
    array = [0]*n 

    for i in range(n):
        line=input()
        # line = inf.readline();
        array[i] = float(line)
 
    array = sorted(array) 
    
    answer = array[0]
    
    while answer > 0:
        count = 0
        for i in range (n):
            count = count + array[i] // answer
    
        if count == k :
            break
        else : 
            answer = answer - 0.00001
    
    answer =round(answer,2)
    print('%.2f' % answer)
    
    return      

def main():
    solution()
    
main()