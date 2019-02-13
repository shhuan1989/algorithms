# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/1/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, M = map(int, input().split())
A = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

cheapest = [(c, i+1) for i, c in enumerate(C)]
cheapest.sort()
cheapest = [i for c, i in cheapest]

counts = {i+1: v for i, v in enumerate(A)}
costs = {i+1: c for i, c in enumerate(C)}
ans = []
ci = 0
for i in range(M):
    t, d = map(int, input().split())
    
    count = counts[t]
    if count > d:
        counts[t] -= d
        ans.append(costs[t] * d)
    else:
        counts[t] = 0
        cost = costs[t] * count
        d -= count
        while ci < len(cheapest):
            dish = cheapest[ci]
            count = counts[dish]
            if count >= d:
                counts[dish] -= d
                cost += d * costs[dish]
                d = 0
                break
            else:
                counts[dish] = 0
                d -= count
                cost += count * costs[dish]
                ci += 1
        cost = 0 if d > 0 else cost
        ans.append(cost)
        
print('\n'.join(map(str, ans)))
