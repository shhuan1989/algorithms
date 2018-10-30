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
const int MAXN = 2e6 + 10;
const int MOD = 1e9+7;

LL fac[MAXN];
bitset<MAXN> vis;
VI primes;

void init() {
    fac[0] = 1;
    rep(i, 1, MAXN) {
        fac[i] = (fac[i-1] * i) % MOD;
    }

    vis.set();
    rep(i, 2, MAXN) {
        if (vis.test(i)) {
            int v = i*2;
            while (v < MAXN) {
                vis.reset(v);
                v += i;
            }
        }
    }

    rep(i, 2, MAXN) {
        if (vis.test(i)) {
            primes.push_back(i);
        }
    }

}

LL my_pow(LL a, LL b) {
    a %= MOD;
    LL ans = 1LL;

    while (b > 0) {
        if (b & 1) {
            ans = (ans * a) % MOD;
        }
        a = (a * a) % MOD;
        b >>= 1;
    }

    return ans;
}

int fact[MAXN+1];
int invfact[MAXN+1];
void remplir_factorielles(){
    fact[0] = 1;
    for (int i = 1; i <= MAXN; i++) {
        fact[i] = ((ll)i * fact[i - 1]) % P;
    }
    invfact[MAXN] = pw(fact[MAXN], P - 2);
    for (int i = MAXN-1; i >= 0; --i) {
        invfact[i] = (invfact[i + 1] * (ll)(i + 1)) % P;
    }
}

int C(int n, int k) {
    return fact[n] * 1ll * invfact[n - k] % P * invfact[k] % P;
}

//#define OFFLINE

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

#ifdef OFFLINE
    ifstream fin("../input.txt");
    cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
#endif

    init();
    int q;
    cin >> q;

    int x, y;
    map<int, map<int, int>> numfactors;
    rep(qi, 0, q) {
        cin >> x >> y;

        map<int, int> factors;

        if (numfactors.find(x) != numfactors.end()) {
            factors = numfactors[x];
        } else{
            int xb = x;
            while (x > 1) {
                bool f = false;
                for (int v: primes) {
                    if (v > x) {
                        break;
                    }
                    if (x % v == 0) {
                        factors[v] += 1;
                        x /= v;
                        f = true;
                        break;
                    }
                }
                if (!f) {
                    factors[x] += 1;
                    break;
                }
            }
            numfactors[xb] = factors;
        }
        LL ans = my_pow(2, y-1);
        for(auto i = factors.begin(); i != factors.end(); i++) {
            ans = ans * ncr(y+i->second-1, i->second);
            ans %= MOD;
        }
        cout << ans << endl;
    }
}