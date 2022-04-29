from heapq import *
import math 

#Implementation of Dijkstra using Adjacency list representation 

def build_graph(v,edges):
    graph={i:[] for i in range(1,v+1)}

    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    return graph

def build_cost(v,edges):
    cost={}
    for i in edges:
        cost[(i[0],i[1])]=i[2]
    
    return cost
            
def dijkstra(v,edges):
    src=1
    graph=build_graph(v,edges)
    cost=build_cost(v,edges)
    dist=[math.inf]*(v+1)
    vis=[False]*(v+1)
    parent=[-1]*(v+1)

    min_heap=[]
    heappush(min_heap,(0,src))
    dist[src]=0

    while min_heap:
        curr_dist,curr_node=heappop(min_heap)
        if vis[curr_node]==False:
            vis[curr_node]=True
            for nbr in graph[curr_node]:   #time-O(V+E)
                if curr_dist+cost[(curr_node,nbr)]<dist[nbr]:
                    dist[nbr]=curr_dist+cost[(curr_node,nbr)]
                    parent[nbr]=curr_node
                    heappush(min_heap,(dist[nbr],nbr))

    print(dist)

if __name__=='__main__':
    edges=[]
    v,e=tuple(map(int,input().split()))
    for i in range(e):
        u,v,w=tuple(map(int,input().split()))
        edges.append([u,v,w])
    dijkstra(v,edges)