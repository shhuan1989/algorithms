# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/6

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

INF = 10 ** 9 + 7

MAXN = 10005
MAXM = 10 ** 5


G = collections.defaultdict(list)

vis = [0 for _ in range(MAXN)]
match = [-1 for _ in range(MAXN)]


def dfs(u, tim):
    for v in G[u]:
        if vis[v] == tim:
            continue
        vis[v] = tim
        if match[v] < 0 or dfs(match[v], tim):
            match[v] = u
            match[u] = v
            return True
        
    return False


if __name__ == '__main__':
    # sys.stdin = open('P2764_10.in', 'r')
    N, M = map(int, input().split())
    
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v+N)
    
    tim = 1
    for i in range(1, N):
        if match[i] < 0:
            dfs(i, tim)
            tim += 1
    
    vis = [False for _ in range(2*N+1)]
    
    ans = 0
    for u in range(1, N+1):
        if vis[u]:
            continue
        
        q = [u]
        ans += 1
        while match[q[-1]] > 0:
            u = q[-1]
            v = match[u]
            q.append(v-N)
            vis[v-N] = True
        
        print(' '.join(map(str, q)))
    
    print(ans)