inf=99999
V=4
G=[[0,2,4,0],
  [2,0,1,3],
  [4,1,0,2],
  [0,3,2,0]]

visited=[0,0,0,0]
visited[0]=True
no_edge=0
cost=0

while (no_edge<V-1):
    x=0
    y=0
    min=inf
    for i in range(V):
        if visited[i]:
            for j in range(V):
                if ((not visited[j]) and G[i][j]):
                    if G[i][j]<min:
                        min=G[i][j]
                        x=i
                        y=j
    print(str(x),"-",str(y),": ",G[x][y])
    cost+=G[x][y]
    no_edge+=1 
    visited[y]=True

print("cost of tree: ",cost)
