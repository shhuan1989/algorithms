
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


//#define OFFLINE

int N;
const int MAXN = 1e5+5;
LL A[MAXN];

const int PN = 1e6+5;
bitset<PN> PRIMES;


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

#ifdef OFFLINE
    ifstream fin("../input.txt");
    cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
#endif

    cin >> N;
    rep(i, 0, N) {
        cin >> A[i];
    }

    PRIMES.set();
    PRIMES.reset(1);
    rep2(i, 2, PN) {
        if (PRIMES[i]) {
            int v = i * 2;
            while (v < PN) {
                PRIMES.reset(v);
                v += i;
            }
        }
    }

    rep(i, 0, N) {
        LL v = A[i];
        LL u = (LL)sqrt(v);

        if (PRIMES.test(u) and u*u == v) {
            cout << "YES" <<endl;
        } else {
            cout << "NO" << endl;
        }

    }

}