from heapq import *
import math 

#Implementation of Dijkstra using matrix representation

def build_graph(v,edges):
    graph=[[-1]*(v+1) for i in range(v+1)]
    for edge in edges:
        i=edge[0]
        j=edge[1]
        w=edge[2]
        graph[i][j]=w
        graph[j][i]=w
    return graph
            
def dijkstra(v,edges):
    src=1
    graph=build_graph(v,edges)
    #cost=build_cost(v,edges)
    dist=[math.inf]*(v+1)
    vis=[False]*(v+1)
    parent=[-1]*(v+1)

    min_heap=[]
    heappush(min_heap,(src,0))
    dist[src]=0

    while min_heap:
        curr_node,curr_dist=heappop(min_heap)
        if vis[curr_node]==False:
            vis[curr_node]=True
            for j in range(1,v+1):
                if graph[curr_node][j]!=-1 and curr_dist+graph[curr_node][j]<dist[j]:
                    dist[j]=curr_dist+graph[curr_node][j]
                    parent[j]=curr_node
                    heappush(min_heap,(j,dist[j]))
    print(dist)

if __name__=='__main__':
    edges=[]
    v,e=tuple(map(int,input().split()))
    for i in range(e):
        u,v,w=tuple(map(int,input().split()))
        edges.append([u,v,w])
    dijkstra(v,edges)