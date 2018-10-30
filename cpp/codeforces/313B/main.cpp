
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

const int MAXN = 1e5+5;

VLL CCOUNT;
VLL presum;
int N;

//#define OFFLINE

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

#ifdef OFFLINE
    ifstream fin("../input.txt");
    cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
#endif

    string s;
    cin >> s;
    cin >> N;

    char p = s[0];
    LL c = 1LL;
    rep(i, 1, s.length()) {
        if (s[i] == s[i-1]) {
            c += 1;
        } else {
            CCOUNT.push_back(c);
            p = s[i];
            c = 1L;
        }
    }
    CCOUNT.push_back(c);

    presum.resize(CCOUNT.size()+1);
    rep(i, 1, CCOUNT.size()+1) {
        presum[i] = presum[i-1] + CCOUNT[i-1];
    }

    rep(i, 0, N) {
        LL l, r;
        cin >> l >> r;
        LL ans = 0;

        int bl = lower_bound(all(presum), l) - presum.begin();
        int br = lower_bound(all(presum), r) - presum.begin();

        ans = presum[br-1] - presum[bl-1] - max(0, br-bl);
        if (bl > 0) {
            ans -= max(0LL, l - presum[bl-1] - 1);
        }
        if (br < CCOUNT.size()+1) {
            ans += max(0LL, r - presum[br-1] - 1);
        }

        cout << ans << endl;





    }

}