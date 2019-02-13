# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/17/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N = int(input())

S = []
sp = []
for i in range(2*N-2):
    s = input()
    if len(s) == N-1:
        sp.append(s)

    S.append((s, i))


S.sort()

def solve(ps, rs):
    prefIdx = {}
    prefVals = {}
    for s, i in S:
        if ps.find(s) == 0:
            prefIdx[len(s)] = i
            prefVals[len(s)] = s
    
    if len(prefIdx) == N-1 and all(rs.find(s) == 0 for s in prefVals.values()) \
            and all(rs.find(S[i][0]) >= 0 for i in range(2*N-2) if i not in prefIdx.values()):
        print(''.join(['P' if i in prefIdx.values() else 'S' for i in range(2*N-2)]))
        exit(0)
    

solve(sp[0], sp[0] + sp[1][-1])
solve(sp[1], sp[1] + sp[0][-1])

