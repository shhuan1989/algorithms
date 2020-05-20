# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/3/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def query(u, v):
    print('? {} {}'.format(u, v))
    sys.stdout.flush()
    w = int(input())
    return w

def solve(N, edges):
    
    degree = [0 for _ in range(N+1)]
    
    def dfs(u, p):
        for v in edges[u]:
            if v != p:
                dfs(v, u)
            degree[v] += 1
    
    def remove(leaf):
        newLeaf = []
        for v in edges[leaf]:
            degree[v] -= 1
            if degree[v] == 1:
                newLeaf.append(v)
            edges[v].remove(leaf)
        edges[leaf] = []
        
        return newLeaf
    
    
    dfs(1, -1)
    
    leafs = [u for u in range(1, N+1) if degree[u] == 1]
    while True:
        if len(leafs) >= 2:
            u, v = leafs[0], leafs[1]
            w = query(u, v)
            if w == u or u == v:
                return w
            else:
                leafs = leafs[2:]
                leafs += remove(u)
                leafs += remove(v)
        else:
            u = leafs[0]
            if not edges[u]:
                return u
            else:
                for v in edges[u]:
                    w = query(u, v)
                    if w == u or w == v:
                        return w
                

N = int(input())
edges = [[] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    
solve(N, edges)