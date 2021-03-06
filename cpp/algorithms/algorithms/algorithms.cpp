#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <functional>
#include <string>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <chrono>
#include <ctime> 

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
	//add_edge(v, u, 0);
}





int dp[101][2700];


int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	auto start = std::chrono::system_clock::now();

	for (int i = 0; i < 26; i++) {
		dp[1][i] = 1;
	}

	int mod = 1000000007;
	for (int i = 2; i < 101; i++) {
		dp[i][0] = 1;
		for (int j = 1; j < 2700; j++) {
			for (int k = 0; k < 26; k++) {
				if (j - k >= 0) {
					dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod;
				}
			}
		}
	}
	auto end = std::chrono::system_clock::now();

	std::chrono::duration<double> elapsed_seconds = end - start;

	std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";
	return 0;
}
