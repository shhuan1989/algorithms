# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/9/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


def solve(A, N):
    ai = collections.defaultdict(list)
    for i, a in enumerate(A):
        ai[a].append(i)
    
    av = list(sorted(set(A)))
    m = av[-1]
    
    ans = 0
    if av[0] == 1:
        for i in range(N-1, -1, -1):
            if A[i] == 1:
                ans = i
                break
        av.pop(0)
    
    for v in av:
        u = v
        i = ai[u][-1]
        c = 0
        while u <= m:
            if u in ai:
                c += bisect.bisect_left(ai[u], i)
            u += v
        ans = max(ans, c)
    
    return ans


T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans.append(solve(A, N))

print('\n'.join(map(str, ans)))

    
    