#Single source shortest path algorithm
#breadth first search in undirected and unweighted graph
#from collections import deque

def bfs(graph,v,src):
    dist=[0]*(vertices+1)
    vis={}
    queue=[]  #queue=deque()
    queue.append(src)
    vis[src]=1

    while queue:
        x=queue.pop(0)  #x=queue.popleft()
        for i in graph[x]:
            if i not in vis:
                dist[i]+=dist[x]+1
                vis[i]=1
                queue.append(i)
    
    print(dist)

if __name__=='__main__':
    edges=[[1,2],[1,3],[3,4]]
    vertices=4
    graph={i:[] for i in range(1,vertices+1)}
    src=1
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    bfs(graph,vertices,src)
