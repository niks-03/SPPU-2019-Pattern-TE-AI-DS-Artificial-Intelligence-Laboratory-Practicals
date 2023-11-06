graph = {
    'A':['C','B','D'],
    'B':['E','F'],
    'C':['G','H'],
    'D':['H'],
    'E':[],
    'F':[],
    'G':[],
    'H':[]
}

visited = []

def dfs(graph, start_node):
    if start_node not in visited:
        print (start_node)
        visited.append(start_node)
        for neighbour in graph[start_node]:
            dfs( graph, neighbour)

dfs( graph, 'A')