//
// Created by shhuan on 2017/11/14.
//

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
#include <numeric>

using namespace std;


#define pub push_back
#define pp pop_back
#define pf push_front
#define ppf pop_front
#define _ inline
#define x first
#define y second
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
#define repd(i, l, r, d) for(int i=l; i<r; i+=d)
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
typedef set<int> SI;
typedef set<long> SL;
typedef set<LL> SLL;
typedef multiset<int> MSI;
typedef multiset<long> MSL;
typedef multiset<LL> MSLL;

struct pt {
	LD x, y;
	pt() {}
	pt(LD x1, LD y1) { x = x1, y = y1; }
	pt operator- (pt nxt) const { return pt(x - nxt.x, y - nxt.y); }
	pt operator+ (pt nxt) const { return pt(x + nxt.x, y + nxt.y); }
	pt operator/ (LD val) const { return pt(x / val, y / val); }
	pt operator* (LD val) const { return pt(x * val, y * val); }
	LD len() { return sqrt(x * x + y * y); }
	LD squareLen() { return x * x + y * y; }
	pt norm(LD val) const { LD tmp = pt(x, y).len(); return pt(x * val / tmp, y * val / tmp); }

	// cross product, a X b
	LD operator% (pt nxt) const { return x * nxt.y - y * nxt.x; }
};


const int INF = 1000000007;
const double eps = 0.000001;
const int MAXN = 1e6 + 5;

int N, Q;
VI A;
VI M;
map<int, VI> numidx;
map<int, int> numcount;

int main() {
    cin >> N;
    A.resize(N);

    rep(i, 0, N) {
        cin >> A[i];
    }

    sort(all(A));

    cin >> Q;
    M.resize(Q);

    int m;
    rep(i, 0, Q) {
        cin >> m;

        int j = upper_bound(all(A), m) - A.begin();
        cout << j << endl;
    }



}