# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    G = collections.defaultdict(list)
    W = collections.defaultdict(int)
    for _ in range(M):
        u, v, w = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        W[u, v] = w
        W[v, u] = w
    
    
    def dfs(u, vis, dist):
        ans = dist
        for v in G[u]:
            if v not in vis:
                ans = max(ans, dfs(v, vis | {v}, dist + W[u, v]))
        
        return ans
    
    
    # print([dfs(i, {i}, 0) for i in range(1, N+1)])
    ans = max([dfs(i, {i}, 0) for i in range(1, N+1)])
    print(ans)
    