# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    sys.stdin = open('P1340_11.in', 'r')
    t0 = time.time()
    N, W = map(int, input().split())
    
    def find(u, parent):
        pu = parent[u]
        if pu == u:
            return u
        pu = find(pu, parent)
        parent[u] = pu
        
        return pu
    
    
    def merge(u, v, parent):
        pu, pv = find(u, parent), find(v, parent)
        if pu != pv:
            parent[pu] = pv
            return True
        return False


    parent = [i for i in range(N)]
    def kruskal(edges):
        if len(edges) < N-1:
            return -1, set()
        
        for i in range(N):
            parent[i] = i
        used = set()
        cost = 0
        added = 0
        for w, u, v, week in sorted(edges):
            if merge(u, v, parent):
                cost += w
                added += 1
                used.add(week)
        
        if added == N-1:
            return cost, used
        
        return -1, set()
    
    
    edges = []
    for week in range(W):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((w, u, v, week))
    
    # edges.sort()
    
    cost, used = kruskal(edges)
    if cost < 0:
        print('\n'.join(map(str, [-1 for _ in range(W)])))
        exit(0)
    
    ans = [cost]
    for week in range(W-1, -1, -1):
        u, v, w, week = edges[week]
        if week in used:
            cost, used = kruskal(edges[:week])
            ans.append(cost)
            if cost < 0:
                ans += [-1] * (W - len(ans))
                break
                pass
        else:
            ans.append(ans[-1])
    
    print('\n'.join(map(str, reversed(ans))))
    
    
    print(time.time() - t0)