def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


def solution(total_sp, skills):
    graph = {}
    for i in range(len(skills)):
        if(skills[i][0] in graph):
            graph[skills[i][0]].append(skills[i][1])
        else:
            graph[skills[i][0]]=[skills[i][1]]
        if(skills[i][1] in graph):
            graph[skills[i][1]].append(skills[i][0])
        else:
            graph[skills[i][1]]=[skills[i][0]]

    answer =  dfs(graph,1)    
    return answer

def main():
    total_sp = 121
    skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]	
    print(solution(total_sp,skills))
    
main()