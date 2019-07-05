#include<bits/stdc++.h>
using namespace std;

const int N=10e6 +3;

vector<int> g[N];
queue <int> q;
vector <bool> vis(N,false);
//only dfs OR bfs
void dfs(int u)
{
	
	cout<< u << " ";
	vis[u]=1;
	for(int v : g[u])
	{
		if(vis[v]) continue;
		dfs(v);
	}
}

void bfs(int u)
{

	q.push(u);
	
	vis[u]=1;
	while(!q.empty())
	{
		int f=q.front();
		q.pop();
		cout<< f << " ";
		for(int i:g[f])
		{
			if(!vis[i])
			{
				q.push(i);
				vis[i]=1;
			}
		}
	}
	
}




int main()
{
	
	cout<< "wait";
	int n,m,u,v;
	cin >> n >> m;	//no. of nodes,edges
	
	while(m--)
	{
		cin >> u >> v ; //connection
		g[u].push_back(v);
		g[v].push_back(u); //exclude if directional tree
		
		
	}
	
	dfs(1);
	
	//if(vis[2]) cout<< "yes"; //are 2 and 1 connected?
	//else cout<< "no";
	
	//bfs(0);


	return 0;
}