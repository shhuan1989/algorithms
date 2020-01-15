# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/14/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, edges):
    
    dsu = collections.defaultdict(int)
    
    def find(u):
        if dsu[u] == 0:
            return u
        
        p = find(dsu[u])
        dsu[u] = p
        return p
    
    def union(u, v):
        pu, pv = find(u), find(v)
        dsu[pu] = pv
        
    def same(u, v):
        return find(u) == find(v)
    
    remove = []
    for u, v in edges:
        if same(u, v):
            remove.append((u, v))
        else:
            union(u, v)
    groups = list(sorted({find(u) for u in range(1, N+1)}))
    added = []
    for u, v in zip(groups[:-1], groups[1:]):
        added.append((u, v))
    
    if not remove:
        print(0)
    else:
        print(len(remove))
        for i in range(len(remove)):
            print('{} {} {} {}'.format(remove[i][0], remove[i][1], added[i][0], added[i][1]))
    

N = int(input())
edges = []
for i in range(N-1):
    u, v = map(int, input().split())
    edges.append((u, v))
solve(N, edges)