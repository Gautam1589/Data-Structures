#Valid for Undirected Graph
#Efficient in finding parent- O(1)

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

if __name__=='__main__':
    edges=[[0,1],[1,2],[1,3],[2,3],[2,5],[3,5],[4,6]]
    vertices=7
    parent=[-1]*7
    for edge in edges: #time - O(E)
        union_set(edge[0],edge[1],parent)
    
    print(parent)