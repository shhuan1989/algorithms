# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/3

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('P2756_6.in', 'r')
    M, N = map(int, input().strip().split())
    
    G = collections.defaultdict(list)
    while True:
        u, v = map(int, input().strip().split())
        if u == -1 and v == -1:
            break
        if 1 <= u <= M and 1 <= v <= N:
            G[u].append(v)
            
    match = [-1 for _ in range(N+1)]
    vis = [-1  for _ in range(N+1)]
    def dfs(u, tim):
        for v in G[u]:
            if vis[v] == tim:
                continue
            vis[v] = tim
            if match[v] < 0 or dfs(match[v], tim):
                match[u] = v
                match[v] = u
                return True
            
        return False
    
    # print(M)
    tim = 1
    for i in range(1, M+1):
        tim += 1
        dfs(i, tim)
    
    
    ans = [(match[u], u) for u in range(M+1, N+1) if match[u] > 0]
    print(len(ans))
    print('\n'.join(['{} {}'.format(u, v) for u, v in ans]))