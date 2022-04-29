import math

def build_graph(n,wells,pipes):
    graph=[[-1]*(n+1) for i in range(n+1)]

    for pipe in pipes:
        h1=pipe[0]
        h2=pipe[1]
        cost=pipe[2]
        graph[h1][h2]=cost
        graph[h2][h1]=cost
    
    for i in range(n):
        graph[0][i+1]=wells[i]
        graph[i+1][0]=wells[i]

    return graph

def find_min(dist,mst_set):
    min_val=math.inf
    idx=-1

    for i in range(len(dist)):
        if mst_set[i]==False and dist[i]<min_val:
            min_val=dist[i]
            idx=i
    return idx

def solve(n,wells,pipes):
    graph=build_graph(n,wells,pipes)
    mst_set=[False]*(n+1)
    dist=[math.inf]*(n+1)

    dist[0]=0

    for i in range(n+1):
        min_idx=find_min(dist,mst_set)
        mst_set[min_idx]=True
        for j in range(n+1):
            if mst_set[j]==False and dist[j]>graph[min_idx][j]:
                dist[j]=graph[min_idx][j]
    
    print(sum(dist))
    
if __name__=='__main__':
    n = 3
    wells=[1,2,2]
    pipes=[[1,2,1],[2,3,1]]
    solve(n,wells,pipes)