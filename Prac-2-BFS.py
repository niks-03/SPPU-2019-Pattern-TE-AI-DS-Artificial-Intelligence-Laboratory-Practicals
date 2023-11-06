graph={
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
queue = []

def bfs( graph, start_node):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        m=queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print('bfs sequence: ')
bfs( graph,'A')