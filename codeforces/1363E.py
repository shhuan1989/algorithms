# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/3

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


N = int(input())
A, B, C = [0], [0], [0]
for i in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

if collections.Counter(B) != collections.Counter(C):
    print(-1)
    exit(0)


g = collections.defaultdict(list)
for i in range(N-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


def dfs2(node, parent):
    if not node:
        return 0, 0, 0
    
    if parent > 0:
        A[node] = min(A[node], A[parent])
    
    totalcost, ttype1, ttype2 = 0, 0, 0
    for child in g[node]:
        if child == parent:
            continue
        cost, type1, type2 = dfs2(child, node)
        totalcost += cost
        ttype1 += type1
        ttype2 += type2
    
    ttype1 += 1 if B[node] == 1 and C[node] == 0 else 0
    ttype2 += 1 if B[node] == 0 and C[node] == 1 else 0
    
    remove = min(ttype1, ttype2)
    totalcost += A[node] * 2 * remove
    
    return totalcost, ttype1 - remove, ttype2 - remove


ans, _, _ = dfs2(1, -1)
print(ans)

