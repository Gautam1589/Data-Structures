def dfs(node,graph,parent,vis,low,dis,bridges,timer):
    vis[node]=True
    dis[node]=timer
    low[node]=timer
    timer+=1

    for nbr in graph[node]:
        if nbr==parent:
            continue
        elif nbr not in vis:
            dfs(nbr,graph,node,vis,low,dis,bridges,timer)
            low[node]=min(low[node],low[nbr])

            if low[nbr]>dis[node]:
                bridges.append([node,nbr])
        else:
            #backedge
            low[node]=min(low[node],dis[nbr])

def find_bridges(edges,v):
    visited={}
    lowest_time=[0]*v
    discovered_time=[0]*v

    timer=0
    graph={i:[] for i in range(v)}

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    bridges=[]
    for node in range(v):
        if node not in visited:
            dfs(node,graph,-1,visited,lowest_time,discovered_time,bridges,timer)

    return bridges

if __name__=='__main__':
    edges=[[0,1],[0,2],[1,2],[1,3],[3,4],[3,6],[4,5],[5,6]]
    vertices=7
    print(find_bridges(edges,vertices))