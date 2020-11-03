# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    g = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    W = [int(x) for x in input().split()]
    MOD = 10007
    ans = 0
    maxv = 0
    for u in range(N):
        n = len(g[u])
        if n <= 1:
            continue
        w = [W[v] for v in g[u]]
        w.sort(reverse=True)
        maxv = max(maxv, w[0] * w[1])
        s = sum(w)
        for v in g[u]:
            ans += W[v] * (s-W[v])
            ans %= MOD
    
    print(maxv, ans)