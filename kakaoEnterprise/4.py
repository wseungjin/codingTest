from collections import defaultdict 

class Graph: 
  
    def __init__(self): 
  
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v,w): 
        self.graph[u].append({"edge" : v , "weight" : w}) 
  
    def DFSUtil(self, v, visited): 
  
        visited[v]= True

        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
    def DFS(self,start,end): 
        V = len(self.graph) 
        print(V)
  
        visited =[False]*(V) 
  
        for i in range(V): 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  


def solution():
    
    answer =0
    
    # inf = open('input.txt');

    # n = inf.readline();
    n = input()
    
    n, m = n.split(" ")    
    n, m = int(n), int(m)
    
    g = Graph() 
    array = []

    for i in range(m):
        line=input()
        # line = inf.readline();
        line = line.split("\n")[0]

        index1 = 0
        index2 = 0
        value1 = line.split(" ")[0]
        value2 = line.split(" ")[1]
        value3 = int(line.split(" ")[2])

        if (value1 in array) :
            index1 = array.index(value1)
        else: 
            array.append(value1)
            index1 = array.index(value1)
            
        if (value2 in array):
            index2 = array.index(value2)
        else: 
            array.append(value2)
            index2 = array.index(value2)        
        g.addEdge(index1, index2 , value3) 


    k=int(input())
    # k = int(inf.readline());
 
    print(array)
    print(g.graph)
 
    for i in range(k):
        line=input()
        # line = inf.readline();
        line = line.split("\n")[0]
        
        value1 = line.split(" ")[0]
        value2 = line.split(" ")[1]
        
        index1 = array.index(value1)
        index2 = array.index(value2)
        g.DFS(index1,index2) 
    return      

def main():
    solution()
    
main()