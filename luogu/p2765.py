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
import math
INF = 10 ** 9 + 7

MAXN = 100005
MAXM = 10 ** 5

G = collections.defaultdict(list)

vis = [0 for _ in range(2*MAXN+1)]
match = [-1 for _ in range(2*MAXN+1)]


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
    # sys.stdin = open('P2765_10.in', 'r')
    N = int(input())
    
    ans = 0
    tim = 1
    pillar = 0
    while True:
        ans += 1
        for u in range(1, ans):
            if int(math.sqrt(u+ans)) ** 2 == u + ans:
                G[ans].append(u+MAXN)
        
        tim += 1
        if not dfs(ans, tim):
            pillar += 1
        
        if pillar > N:
            break
    
    # print(match[1:ans])
    # print(match[1+MAXN: ans+MAXN])
    
    vis = [False for _ in range(2 * MAXN + 1)]
    print(ans-1)
    for u in range(1, ans):
        if vis[u]:
            continue
        
        q = [u]
        ans += 1
        while match[q[-1]+MAXN] > 0:
            v = match[q[-1] + MAXN]
            q.append(v)
            vis[v] = True
        
        print(' '.join(map(str, q)))
