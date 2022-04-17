#Kruskal's algorithm
#Valid for Undirected weighted Graph
#using path compression technique in union set
#finding minimum cost spanning tree (MST)

def find_set(node,parent): #time - O(1)
    if parent[node]==-1:
        return node
    return find_set(parent[node],parent)

def union_set(u,v,parent):
    if u>v:
        u,v=v,u
    p_u=find_set(u,parent)
    p_v=find_set(v,parent)

    if p_u!=p_v:
        parent[p_v]=p_u

def kruskals_mst(edges):
    edges.sort(key=lambda x:x[2])
    parent=[-1]*(6+1)
    mstcost=0
    for edge in edges: #time - O(E)
        u=edge[0]
        v=edge[1]
        w=edge[2]

        if find_set(u,parent)!=find_set(v,parent):
            mstcost+=w
            union_set(u,v,parent)
    print(mstcost)

if __name__=='__main__':
    edges=[[1,2,1],[1,3,2],[1,4,2],[2,3,2],[2,4,3],[3,4,3]]
    vertices=6
    kruskals_mst(edges)