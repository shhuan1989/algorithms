#include <iostream>
#include <algorithm>
#include <map>
#include <set>


using namespace std;

const int INF = 1000000007;
const double eps = 0.000001;
const int MAXN = 200005;


int N;
int V;

int presum[MAXN];
int ksv[MAXN];


int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);

	string s;
	cin >> s;
	size_t N = s.length();
	for (int i = 0; i < N; i++)
	{
		presum[i + 1] = presum[i] + (s[i] == '1' ? 1 : 0);
	}

	long ans = 0l;
	int K = 50;
	for (int k = 1; k <= K; k++) {
		map<long, int> wc;
		for (int i = 0; i <= N; i++) {
			int v = i - k * presum[i];
			wc[v] += 1;
		}
		for (auto v = wc.begin(); v != wc.end(); v++)
		{
			int u = v->second;
			ans += u * (u - 1) / 2;
		}
	}

	for (int i = 0; i <= N; i++)
	{
		ksv[i] = i - K * presum[i];
	}

	set<pair<int, int>> m, sm;
	for (int i = N; i >= 0; i--) {
		pair<int, int> cp = make_pair(ksv[i], i);
		for (auto p = m.lower_bound(cp); p != m.end(); p++)
		{
			int j = p->second;
			int l = j - i;
			int d = presum[j] - presum[i];
			if (d > 0 && l % d == 0 && l / d > K) {
				ans += l;
			}
		}
		sm.insert(cp);
		if (i > 0 && s[i-1] == '1') {
			m.insert(sm.begin(), sm.end());
			sm.clear();
		}
	}

	cout << ans << endl;
	return 0;
}
