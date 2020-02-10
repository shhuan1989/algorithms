# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/26/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

sys.setrecursionlimit(10**5+1)

def solve(N, C, edges):
    
    ans = [0 for _ in range(N)]
    def dfs(curr, parent):
        wc = collections.defaultdict(int)
        for v in edges[curr]:
            if v != parent:
                nwc = dfs(v, curr)
                for w, c in nwc.items():
                    wc[w] += c
        wc[C[curr]] += 1
        mx = max(wc.values())
        ans[curr] = sum([w for w, c in wc.items() if c == mx])
        
        return wc
    
    dfs(0, -1)
    
    print(' '.join(map(str, ans)))


N = int(input())
C = [int(x) for x in input().split()]
edges = [[] for _ in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)
    

solve(N, C, edges)