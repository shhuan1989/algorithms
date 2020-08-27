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

#define MAXN 50005
#define MAXM 200000
#define INF 1000000007
#define LL long long
#define ll long long

using namespace std;

int wc[1000];

int main() {
	std::cin.tie (0);
	ios_base::sync_with_stdio(false);

	fill_n(wc, 1000, 0);
	int n, m;
	cin >> n >> m;
	int v;
	for (int i = 0; i < m; ++i) {
		cin >> v;
		wc[v] += 1;
	}

	for (int i = 0; i < 1000; ++i) {
		for (int j = 0; j < wc[i]; ++j) {
			cout << i << " ";
		}
	}
	cout << endl;

	return 0;
}
