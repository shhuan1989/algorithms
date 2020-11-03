# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/23

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List

if __name__ == '__main__':
    N = int(input())
    
    idmem = {}
    idv = [0]
    
    def getid(key):
        if key in idmem:
            return idmem[key]
        
        idv[0] += 1
        idmem[key] = idv[0]
        
        return idv[0]
        
        
    couple = []
    G = collections.defaultdict(list)
    for _ in range(N):
        u, v = input().strip().split()
        u, v = getid(u), getid(v)
        couple.append((u, v))
        G[u].append(v)
    
    M = int(input())
    for _ in range(M):
        u, v = input().strip().split()
        u, v = getid(u), getid(v)
        G[v].append(u)
    
    
    dfn = [-1 for _ in range(idv[0] + 1)]
    low = [-1 for _ in range(idv[0] + 1)]
    idx = [0]
    s = []
    instack = [False for _ in range(idv[0] + 1)]
    group = [0]
    belongs = [-1 for _ in range(idv[0] + 1)]
    
    def tarjan(u):
        idx[0] += 1
        dfn[u] = idx[0]
        low[u] = idx[0]
        s.append(u)
        instack[u] = True
        
        for v in G[u]:
            if dfn[v] < 0:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif instack[v]:
                low[u] = min(low[u], dfn[v])
        
        if low[u] == dfn[u]:
            group[0] += 1
            while s and s[-1] != u:
                belongs[s[-1]] = group[0]
                instack[s[-1]] = False
                s.pop()
            if s:
                belongs[s[-1]] = group[0]
                instack[s[-1]] = False
                s.pop()
    
    
    for u in range(1, idv[0]+1):
        if dfn[u] < 0:
            tarjan(u)
    
    # print(belongs)
    # print(couple)
    # print(idv[0])
    for u, v in couple:
        if belongs[u] == belongs[v]:
            print('Unsafe')
        else:
            print('Safe')
                
            
            
        
        