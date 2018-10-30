#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <ostream>
#include <istream>
#include <typeinfo>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <limits>
#include <fstream>
#include <array>
#include <list>
#include <bitset>
#include <functional>
#include <random>
using namespace std;


#define pb push_back
#define pp pop_back
#define pf push_front
#define ppf pop_front
#define _ inline
#define fst first
#define sec second
#define ins insert
#define ers erase
#define mp make_pair
#define mt make_tuple
#define all(u) (u).begin(), (u).end()
#define rall(u) (u).rbegin(), (u).rend()
#define sz size
#define rsz resize
#define pw2(u) (1<<(u))
#define chcpy(Vec) copy(Vec.begin(), Vec.end(), ostream_iterator<char>(cout))
#define intcpy(Vec) copy(Vec.begin(), Vec.end(), ostream_iterator<int>(cout, " "))
#define elif else if
#define uset unordered_set
#define umap uorderd_map
#define rep(i, l, r) for(int i=l; i<r; i++)
#define rep2(i, l, r) for(int i=l; i<=r; i++)
#define rrep(i, l, r) for(int i=l; i>r; i--)
#define rrep2(i, l, r) for(int i=l; i>=r; i--)


typedef long L;
typedef long long LL;
typedef pair<int, int> PII;
typedef pair<long, long> PLL;
typedef double LD;
typedef unsigned int UINT;
typedef unsigned long long ULL;
typedef unsigned long UL;
typedef vector<vector<int>> VVI;
typedef vector<vector<UINT>> VVUINT;
typedef vector<vector<L>> VVL;
typedef vector<vector<LL>> VVLL;
typedef vector<int> VI;
typedef vector<long> VL;
typedef vector<LL> VLL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
typedef vector<LD> VLD;
typedef vector<bool> VB;
typedef tuple<LL, LL, LL> TLLL;
typedef tuple<int, int, int> TIII;

const int INF = 1000000007;
const double eps = 0.000001;

const int MAXN = 1e6+5;




VPLL G[MAXN];
int N, M;
stack<int> st;
bitset<MAXN> instack;
int belongs[MAXN], dfn[MAXN], low[MAXN], dindex, sccIndx;


void tarjan(int u) {
    dfn[u] = low[u] = dindex++;
    st.push(u);
    instack.set(u);
    for (PLL vw : G[u]) {
        int v = vw.first;
        if (dfn[v] == -1) {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        } else if (instack.test(v)) {
            low[u] = min(low[u], dfn[v]);
        }
    }

    if (dfn[u] == low[u]) {
        int idx;
        do {
            idx = st.top();
            st.pop();
            instack.reset(idx);
            belongs[idx] = sccIndx;
        } while (idx != u);
        sccIndx++;
    }
}


inline void initTarjan() {
    memset(dfn, -1, sizeof(dfn));
}


bitset<MAXN> componentProcessed;
VPLL compressedGraph[MAXN];
LL componentCost[MAXN];

inline LL getCost(LL initCost) {
    // x = initCost
    // s = x + x-1 + x-1-2 + x-1-2-3 + x-1-2-3-4 + ...
    // x-(1+2+...+y) == 0
    // => (1+y)*y/2 <= x
    // s = x*y - (1 + (1+2) + (1+2+3) + ... + (1+2+...+y))
    //   = x*y - m

    //    2m = sigma(i(i+1)), i = 0, ..., y
    //       = sigma(i^2 + i), i = 0, ..., y
    //    a = sigma(i^2) , i=0, ..., y
    //      = y*(y+1)*(2y+1)/6
    //    b = sigma(i), i=0, ..., y
    //      = y(y+1)/2
    //
    //    a + b = y(y+1)(2y+1+3)/6
    //          = y(y+1)(y+2)/3
    //    s = (a+b)/2 = y(y+1)(y+3)/6

    LL lo = 0, hi = 1000000LL;
    while (lo < hi) {
        LL mid = (lo + hi + 1) >> 1;
        if ((mid * (mid-1)) / 2LL <= initCost) {
            lo = mid;
        } else {
            hi = mid-1;
        }
    }
    return initCost*lo - lo*(lo+1)*(lo-1) / 6LL;
}

// TLE
LL getCost2(LL initCost) {
    LL ans = 0LL;
    LL d = 1LL;
    while (initCost > 0) {
        ans += initCost;
        initCost -= d;
        d += 1L;
    }

    return ans;
}


LL memo[MAXN];

// find the longest path starts from given vertex
LL func(int u) {
    if (memo[u] != -1) {
        return memo[u];
    }

    memo[u] = componentCost[u];
    rep(i, 0, compressedGraph[u].size()) {
        int v = compressedGraph[u][i].first;
        LL w = compressedGraph[u][i].second;
        memo[u] = max(memo[u], func(v) + w + componentCost[u]);
    }

    return memo[u];
}


//#define OFFLINE

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

#ifdef OFFLINE
    ifstream fin("../input.txt");
    cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
    freopen("../input.txt","r",stdin);
#endif

    initTarjan();
    scanf("%d %d", &N, &M);
    rep(i, 0, M) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);;
        G[u].push_back(mp(v, w)); // maybe exist multiple edges between same u,v
    }

    rep2(i, 1, N) {
        if (dfn[i] == -1) {
            tarjan(i); // find scc, strong connected component
        }
    }

    int s;
    scanf("%d", &s);
    rep2(u, 1, N) {
        rep(j, 0, G[u].size()) {
            int v = G[u][j].first;
            if (belongs[u] != belongs[v]) { // u and v not in same scc
                compressedGraph[belongs[u]].push_back(mp(belongs[v], G[u][j].second));
            } else {
                componentCost[belongs[u]] += getCost(G[u][j].second); // w, w-1, w-2, w-3, ..., 0
            }
        }
    }

    memset(memo, -1, sizeof(memo));
    printf("%lld\n", func(belongs[s]));

    return 0;
}





























