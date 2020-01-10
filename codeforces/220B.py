# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/8/20

for each query l, r; how many x that count of x in range [l, r] equals x

for each query ends with x, query (l, x) with Fenwick tree

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, A, Q):
    
    bit = [0 for _ in range(N)]
    
    def add(index, val):
        while index < N:
            bit[index] += val
            index |= index + 1
        
    def query(index):
        index = min(index, N-1)
        s = 0
        while index >= 0:
            s += bit[index]
            index = (index & (index + 1)) - 1
        
        return s
    
    q = collections.defaultdict(list)
    for i, (l, r) in enumerate(Q):
        q[r].append((l, i))
    
    ans = [0 for _ in range(M)]
    vi = collections.defaultdict(list)
    for i, v in enumerate(A):
        u = vi[v]
        u.append(i)
        lv = len(vi[v])
        if lv >= v:
            add(u[-v], 1)
            if lv >= v + 1:
                add(u[-v-1], -2)
            if lv >= v + 2:
                add(u[-v-2], 1)
        
        for l, qi in q[i]:
            ans[qi] = query(i) - query(l-1)
    
    print('\n'.join(map(str, ans)))


def test():
    N, M = 100000, 100000
    import random
    A = [random.randint(0, 1000) for _ in range(N)]
    Q = []
    for i in range(M):
        l = random.randint(0, N-1)
        r = random.randint(l, N-1)
        Q.append((l, r))
    solve(N, M, A, Q)

# test()


N, M = map(int, input().split())
A = [int(x) for x in input().split()]
Q = []
for i in range(M):
    l, r = map(int, input().split())
    Q.append((l-1, r-1))
    
solve(N, M, A, Q)