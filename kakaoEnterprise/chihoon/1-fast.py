from math import ceil, log


def minimum(trees,node,start, end, left, right ): 
    if start > right or end < left: return 1000000000 
    
    if left <= start and right >= end: return trees[node] 
    
    mid = (start + end)//2 
    
    return min(minimum(trees, node*2,start, mid, left, right), minimum(trees, node*2 + 1,mid+1, end, left, right)) 

def init(arr,trees,node,start,end): 
    
    if start == end :
        trees[node] = arr[start]
        return trees[node]
    
    mid = (start + end) // 2
    trees[node] = min(init(arr,trees,node*2,start,mid),init(arr,trees,node*2+1,mid+1,end))
    return trees[node]

def solution(x,spaces):
    N = len(spaces)
    
    h = int(ceil(log(N,2)))
    size = pow(2,h)
    sizeMax = size * 2 

    trees = [0] * sizeMax
    init(spaces,trees,1,0,N-1)
        
    maxValue = -1
    for start in range(len(spaces) - x + 1):
        maxValue = max(maxValue,minimum(trees,1,0,N -1,start,start + x - 1))
            
    return maxValue

def main():
    print(solution(2,[8,2,4,6])) 
    print(solution(1,[1,2,3,1,2]))
    print(solution(2,[1,1,1]))
    print(solution(3,[2,5,4,6,8]))

main()