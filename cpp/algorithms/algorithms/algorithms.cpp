#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <functional>
#include <string>
#include <stdio.h>
#include <string.h>


using namespace std;

const int INF = 1000000007;
const double eps = 0.000001;
const int MAXN = 200005;
const int MAXM = 2000000;

int head[MAXN];
bool vis[MAXN];
int dep[MAXN];
int cur[MAXN];

int nxt[MAXM];
int cap[MAXM];
int to[MAXM];

int tot = 1;

void add_edge(int u, int v, int w) {
	tot++;

	to[tot] = v;
	cap[tot] = w;
	nxt[tot] = head[u];
	head[u] = tot;
}

void add(int u, int v, int w) {
	add_edge(u, v, w);
	add_edge(v, u, 0);
}


bool bfs(int start, int end) {
	fill_n(vis, MAXN, false);
	fill_n(dep, MAXN, -1);

	deque<int> q;
	q.push_back(start);
	vis[start] = true;
	dep[start] = 0;
	while (q.size()) {
		int u = q.front();
		q.pop_front();
		for (int i = head[u]; i > 0; i = nxt[i]) {
			int v = to[i];
			if (cap[i] > 0 && dep[v] < 0)
			{
				dep[v] = dep[u] + 1;
				q.push_back(v);
			}
		}
	}

	return dep[end] > 0;
}


int dfs(int u, int end, int a) {
	if (u == end || a <= 0) {
		return a;
	}

	int flow = 0;
	for (int i = cur[u]; i > 0 && a > 0; i = nxt[i])
	{
		cur[u] = i;
		int v = to[i];
		if (cap[i] > 0 && dep[v] == dep[u] + 1)
		{
			int f = dfs(v, end, min(a, cap[i]));
			if (f > 0) {
				a -= f;
				flow += f;
				cap[i] -= f;
				cap[i ^ 1] += f;
			}
		}
	}

	return flow;
}


int dinic(int start, int end) {
	int flow = 0;
	while (bfs(start, end))
	{
		for (int u = 0; u < MAXN; u++)
		{
			cur[u] = head[u];
		}
		flow += dfs(start, end, INF);
	}

	return flow;
}

int barrier[205][205];

int dx[8]{-1, -2, -2, -1, 1, 2, 2, 1};
int dy[8]{-2, -1, 1, 2, 2, 1, -1, -2};

int getid(int x, int y, int n) {
	return (x - 1) * n + y;
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	int n, m;
	cin >> n >> m;

	for (size_t i = 0; i < 205; i++)
	{
		for (size_t j = 0; j < 205; j++)
		{
			barrier[i][j] = false;
		}
	}

	for (size_t i = 0; i < m; i++)
	{
		int x, y;
		cin >> x >> y;
		barrier[x][y] = true;
	}

	int start = 0;
	int end = n * n + 1;

	for (int x = 1; x <= n; x++) {
		for (int y = 1; y <= n; y++) {
			if (barrier[x][y])
			{
				continue;
			}
			int u = getid(x, y, n);
			if ((x + y) % 2 == 1) {				
				add(start, u, 1);
				for (int i = 0; i < 8; i++)
				{
					int nx = x + dx[i];
					int ny = y + dy[i];
					if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && !barrier[nx][ny])
					{
						add(u, getid(nx, ny, n), INF);
					}
				}
			}
			else {
				add(u, end, 1);
			}
		}
	}

	cout << n * n - m - dinic(start, end) << endl;

	return 0;
}
