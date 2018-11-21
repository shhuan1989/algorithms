# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/21/18


Fenwick Tree

prefix sum in s
j < i, s[i]-s[j] < t,

i+1 - (c = count of j that makes s[i]-s[j] >= t)
c = count of s[j] <= s[i] - t


# in this way, BIT doesn't support 0-based indexing,
# but i & (i+1)-1 and i|(i+1) does.
def lowbit(i):
    return i & (-i)
    
    
# finding sum
struct FenwickTree {
    vector<int> bit;  // binary indexed tree
    int n;

    void init(int n) {
        this->n = n;
        bit.assign(n, 0);
    }
    int sum(int r) {
        int ret = 0;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret += bit[r];
        return ret;
    }
    void add(int idx, int delta) {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] += delta;
    }
    int sum(int l, int r) {
        return sum(r) - sum(l - 1);
    }
    void init(vector<int> a) {
        init(a.size());
        for (size_t i = 0; i < a.size(); i++)
            add(i, a[i]);
    }
};

#finding minimum
struct FenwickTreeMin {
    vector<int> bit;
    int n;
    const int INF = (int)1e9;
    void init(int n) {
        this->n = n;
        bit.assign(n, INF);
    }
    int getmin(int r) {
        int ret = INF;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret = min(ret, bit[r]);
        return ret;
    }
    void update(int idx, int val) {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] = min(bit[idx], val);
    }
    void init(vector<int> a) {
        init(a.size());
        for (size_t i = 0; i < a.size(); i++)
            update(i, a[i]);
    }
};

# find sum in 2d
struct FenwickTree2D {
    vector<vector<int>> bit;
    int n, m;
    // init(...) { ... }
    int sum(int x, int y) {
        int ret = 0;
        for (int i = x; i >= 0; i = (i & (i + 1)) - 1)
            for (int j = y; j >= 0; j = (j & (j + 1)) - 1)
                ret += bit[i][j];
        return ret;
    }
    void add(int x, int y, int delta) {
        for (int i = x; i < n; i = i | (i + 1))
            for (int j = y; j < m; j = j | (j + 1))
                bit[i][j] += delta;
    }
};

"""
import bisect

N, T = map(int, input().split())

A = [int(x) for x in input().split()]

prefsums = [0] * (N + 1)
for i in range(N):
    prefsums[i + 1] = A[i] + prefsums[i]

MAXNN = len(prefsums) + 1
L = [0] * MAXNN


def lsb(i):
    return i & (-i)


def update(i):
    while i < MAXNN:
        L[i] += 1
        i |= i + 1


def get(i):
    ans = 0
    while i >= 0:
        ans += L[i]
        i = (i & (i + 1)) - 1
    
    return ans


prefsums = list(sorted(set(prefsums)))
ans = 0
update(bisect.bisect_left(prefsums, 0))

pr = 0
for i, v in enumerate(A):
    pr += v
    npos = bisect.bisect_right(prefsums, pr - T)
    ans += i + 1 - get(npos - 1)
    k = bisect.bisect_left(prefsums, pr)
    update(k)

print(ans)


