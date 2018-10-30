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
#include <string>
#include <tuple>
#include <string.h>

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
const int MAXN = 300;

//#define OFFLINE

int A[MAXN][MAXN];
int ans[MAXN];
int f[MAXN][MAXN][2][MAXN];


int bisect_right(int* arr, int n, int val) {
    int l = 0;
    int r = n + 1;
    while (l < r) {
        int m = (l + r) / 2;
        if (arr[m] <= val) {
            l = m + 1;
        }
        else {
            r = m;
        }
    }

    return l;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    int mxMN = max(M, N);
    int mnMN = min(M, N);
    memset(ans, 1000000, sizeof(ans[0]) * MAXN);
    memset(f, 0, sizeof(f[0][0][0][0]) * MAXN * MAXN * 2 * MAXN);
    ans[0] = 0;

    rep(i, 0, N) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            A[i][j] = s[j] - '0';
        }
    }

    rep2(width, 1, mnMN) {
        rep2(color, 0, 1) {
            rep2(sr, 0, N - width) {
                rep2(sc, 0, M - width) {
                    int steps = f[sr + 1][sc + 1][color][width - 1];

                    int cc = color;
                    rep(c, sc, sc + width) {
                        steps += (A[sr][c] == cc) ? 0 : 1;
                        cc ^= 1;
                    }

                    cc = color ^ 1;
                    rep(r, sr + 1, sr + width) {
                        steps += (A[r][sc] == cc) ? 0 : 1;
                        cc ^= 1;
                    }
                    f[sr][sc][color][width] = steps;
                    ans[width] = min(ans[width], steps);
                }
            }
        }
    }

    int qc;
    cin >> qc;
    rep(i, 0, qc) {
        int q;
        cin >> q;

        cout << bisect_right(ans, mnMN, q) - 1 << endl;
    }

}