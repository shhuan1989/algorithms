
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
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz size
#define rsz resize
#define pw2(x) (1<<(x))
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

int n, m;
int l[MAXN];
VVLL dist;
VVLL presum;

LL solve(int start, LL hval) {
    if (start > n || start < 1 || hval < 0) {
        return 0;
    }

    int p = lower_bound(all(dist[start]), hval) - dist[start].begin();

    return hval*p - presum[start][p];
}


//#define OFFLINE

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

#ifdef OFFLINE
    ifstream fin("../input.txt");
    cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
#endif

    cin >> n >> m;

    dist.resize(n+1);
    presum.resize(n+1);

    rep2(i, 2, n) {
        cin >> l[i];
    }

    rep2(i, 1, n) {
        int u = i;
        LL d = 0LL;
        while (u > 0) {
            dist[u].push_back(d);
            d += l[u];
            u /= 2;
        }
    }

    rep2(i, 1, n) {
        int u = i;
        presum[i].resize(dist[u].size()+1);
        LL d = 0LL;
        sort(all(dist[u]));

        rep(j, 0, dist[u].size()) {
            presum[i][j+1] = presum[i][j] + dist[u][j];
        }
    }

    int a, h;
    rep(i, 0, m) {
        cin >> a >> h;
        LL ans = 0LL;
        ans += solve(a, h);

        while (a > 1) {
            int fa = a/2;
            h -= l[a];
            if (h < 0) {
                break;
            }
            ans += h;

            if (fa * 2 == a && fa*2+1 <= n) {
                // a is left child of fa
                ans += solve(fa*2+1, h-l[fa*2+1]);
            }

            if (fa*2+1 == a) {
                // a is right child of fa
                ans += solve(fa*2, h-l[fa*2]);
            }

            a = fa;
        }

        cout << ans << endl;
    }
}