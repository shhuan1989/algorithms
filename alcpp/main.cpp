#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <fstream>

#define MAXN 500005
#define MAXM 1000005
#define INF 1000000007
#define LL long long
#define ll long long
#define N 500008

using namespace std;

ll n,m,ans;
ll to[N];
struct node{
	ll to,nex;
}e[N];
ll x,y,tot;
ll head[N];
bool vis[N];
void add(ll a,ll b)
{
	e[++tot].to=b;
	e[tot].nex=head[a];
	head[a]=tot;
}
bool find(ll x)
{
	ll xx;
	for(ll i=head[x];i;i=e[i].nex)
	{
		xx=e[i].to;
		if(!vis[xx])
		{
			vis[xx]=1;
			if(!to[xx]||find(to[xx]))
			{
				to[xx]=x;
				return 1;
			}
		}
	}
	return 0;
}

int main() {
	std::cin.tie (0);
	ios_base::sync_with_stdio(false);

//	read(n);read(m);
//	read(x);read(y);
	cin >> n >> m;
	cin >> x >> y;
	while(x!=-1&&y!=-1)
	{
		if(x<=n&&y<=m) add(x,y);
//		read(x);read(y);
		cin >> x >> y;
	}
	for(ll i=1;i<=n;i++)
	{
		memset(vis,0,sizeof(vis));
		if(find(i)) ans++;
	}
	cout<<ans<<endl;
	for(ll i=n+1;i<=m;i++)
	{
		if(to[i]) cout<<to[i]<<" "<<i<<endl;
	}

	return 0;
}
