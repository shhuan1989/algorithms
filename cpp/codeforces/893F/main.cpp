#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;


#define all(x) (x).begin(), (x).end()
#define rep(i, l, r) for(int i=l; i<r; i++)
#define rep2(i, l, r) for(int i=l; i<=r; i++)
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<int> VI;
typedef vector<vector<LL>> VVLL;

const int MAXN = 1e6+5;
int n, r, m;
VI A;
int l[MAXN]; // l[u] is distance between node u and its parent u/2
map<int, map<int, VLL>> dist; // dist[u] is distance from u to all nodes in its subtree
map<int, VLL> presum; // presum[u][j] is sum for previous j items in dist[u]

map<int, vector<int>> graph;
LL solve(int start, LL hval) {
    if (start > n || start < 1 || hval < 0) {
        return 0;
    }
    // binary search to find the first value greater than hval
    // O(log(n))
//    int p = lower_bound(all(dist[start]), hval) - dist[start].begin();
//    return hval*p - presum[start][p];
}


VLL dfs(int u, int fa, int d) {
    VLL ans;
    for (int v: graph[u]) {
        if (v != fa) {
            VLL vx = dfs(v, fa, d+1);
            for(LL x: vx) {
                ans.push_back(x);
            }
        }
    }
    dist[u][d] = ans;
    return ans;
}

//#define OFFLINE
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
#ifdef OFFLINE
    ifstream fin("../input.txt");
    cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
#endif
    cin >> n >> r;
    A.resize(n);
    rep(i, 0, n) {
        cin >> A[i];
    }

    int x, y;
    rep(i, 0, n-1) {
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    dfs(r, -1);

    // O(n*log(n)*loglog(n))
    rep2(i, 1, n) {
        int u = i;
        presum[i].resize(dist[u].size()+1);
        LL d = 0LL;
        sort(all(dist[u]));
        rep(j, 0, dist[u].size()) {
            presum[i][j+1] = presum[i][j] + dist[u][j];
        }
    }

    cin >> m;
    int p, q, k;
    LL last = 0;
    rep(i, 0, m) {
        cin >> p >> q;
        x = ((p+last) % n) + 1;
        k = (q+last) % n;

        last = solve(x, k);
        cout << last << endl;
    }
}