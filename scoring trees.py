'''
from a node, find the maximun score that can be 
achieved by dfs.
score=weight[parent]+max(weight[child])


input:
11
1 2
1 3
1 4
2 5
2 6
3 7
4 9
7 8
9 10
9 11
1
2
3
4
5
6
7
8
9
10
11
{1: 25, 2: 8, 5: 5, 6: 6, 3: 18, 7: 15, 8: 8, 4: 24, 9: 20, 10: 10, 11: 11}
'''

from collections import defaultdict

vis={}
g=defaultdict(list)
def dfs(u):
    
    score[u]=weight[u]
    mx=0
    vis[u]=True
    for child in g[u]:
    	if(child in vis):
    		continue
    	dfs(child)
    	mx=max(mx,score[child])
    score[u]+=mx

n=int(input()) #number of nodes
m=n-1 # number of edges

while(m):
    m=m-1
    a,b=map(int,input().split()) #edges
    g[a].append(b)
    
    
weight={}
score={}

#weight=list(map(int,input().split()))
for i in range(1,n+1):
	weight[i]=int(input())
dfs(1)
print(score)
