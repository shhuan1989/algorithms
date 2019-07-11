# -*- coding:utf-8 -*-

"""
ID: shuangq1
LANG: PYTHON3
TASK: shuttle
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
import math
import time

t0 = time.time()

# fin = open('shuttle.in', 'r')
# fout = open('shuttle.out', 'w')


N, M = map(int, input().split())
G = collections.defaultdict(set)
C = [[0 for _ in range(50)] for _ in range(50)]
for mi in range(M):
    s, t, c = map(int, input().split())
    G[s].add(t)
    C[s][t] = c
    

def dfs(parent, current, maxflow):
    if current == N:
        return True, maxflow
    
    if maxflow <= 0:
        return False, 0
    
    for child in G[current]:
        a, b = dfs(current, child, min(maxflow, C[current][child]))
        if a:
            C[current][child] -= b
            C[child][current] += b
            G[child].add(current)
            return True, b
    
    return False, 0


maxflow = 0
while True:
    a, b = dfs(0, 1, 1000000)
    if a:
        maxflow += b
    else:
        break
        
print(maxflow)
    

    

# fout.close()
#
# fin.close()
# fout.close()

print(time.time() - t0)
exit(0)
