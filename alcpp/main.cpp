#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <fstream>

#define MAXN 500005
#define MAXM 1000005
#define INF 1000000007

using namespace std;

int lp[MAXN];
vector<int> pr;

int mypow(int a, int b) {
	if (a == 0) {
		return 0;
	}
	if (b == 0) {
		return 1;
	}

	int c = mypow(a, b/2);

	return b % 2 == 0 ? c * c : c * c *a;
}

long long mypow(long long b, long long p, long long k) {
	if (b == 0) {
		return 0;

	}
	if (p == 0) {
		return 1LL;
	}

	long long h = mypow(b, p/2, k);
	long long s = (h * h) % k;
	return p % 2 == 0 ? s : (s*b) % k;
}

int main() {
	std::cin.tie (0);
	ios_base::sync_with_stdio(false);

	int b, p, k;
	cin >> b >> p >> k;
	cout << b << "^" << p << " mod " << k << "=" << mypow(b, p, k) % k << endl;

	return 0;
}
