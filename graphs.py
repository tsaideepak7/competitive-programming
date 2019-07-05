import queue #put,get
from collections import defaultdict

q=queue.Queue()
g=defaultdict(list)
vis={}

def dfs(u):
    print(u)
    vis[u]=True
    for v in g[u]:
        if( v in vis):
            continue
        dfs(v)

def bfs(u):
    q.put(u)
    while(not q.empty()):
        f=q.get()
        print(f)
        vis[f]=True
        for v in g[f]:
            if(v in vis):
                continue
            q.put(v)
        
    

n,m=map(int,input().split()) #no. of nodes,edges


while(m):
    m=m-1
    a,b=map(int,input().split()) #edges
    g[a].append(b)
    g[b].append(a)

#dfs(1)
#bfs(1)



