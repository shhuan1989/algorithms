#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans;
        if (temperatures.empty()) {
            return ans;
        }

        ans.resize(temperatures.size());
        for (int i = 0; i < temperatures.size(); i++) {
            ans[i] = 0;
        }

        int maxa = 0;
        set<int> b;
        map<int, vector<int>> vi;
        for (int i = 0; i < temperatures.size(); ++i) {
            maxa = max(maxa, temperatures[i]);
            b.insert(temperatures[i]);
            vi[temperatures[i]].push_back(i);
        }

        vector<int> c;
        c.reserve(b.size());
        for (auto i = b.begin(); i != b.end(); i++) {
            c.push_back(*i);
        }
        sort(c.begin(), c.end());

        for (int i = 0; i < temperatures.size(); ++i) {
            int u = temperatures[i];
            auto mv = upper_bound(c.begin(), c.end(), u);
            for (auto j = mv; j != c.end(); j++) {
                int v = *j;
                vector<int> ids = vi[v];
                auto m = upper_bound(ids.begin(), ids.end(), i);
                if (m != ids.end()) {
                    if (ans[i] != 0) {
                        ans[i] = min(ans[i], *m-i);
                    } else {
                        ans[i] = *m-i;
                    }
                }
            }
        }


        return ans;


    }
};

int main() {
    Solution s;
    vector<int> v = {73, 74, 75, 71, 69, 72, 76, 73};

    vector<int> ans = s.dailyTemperatures(v);
    for (auto i = ans.begin(); i != ans.end(); i ++) {
        cout << *i << " ";
    }
    return 0;
}