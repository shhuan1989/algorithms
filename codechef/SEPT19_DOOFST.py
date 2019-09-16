# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/12/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

N, M = map(int, input().split())
A = collections.defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)
    


k = 0
ans = []
done = False
while (k+1)*N <= 10**6 and not done:
    mark = [0] * (N+1)
    for i in range(1, N+1):
        if mark[i] != 0 or not A[i]:
            continue
            
        m = 1
        q = [i]
        while q:
            nq = []
            for u in q:
                mark[u] = m
                for v in A[u]:
                    if mark[v] == 0:
                        nq.append(v)
            q = nq
            m = 1 if m == 2 else 2
    
    for i in range(1, N+1):
        if mark[i] == 2:
            mark[i] = 0
    ans.append(''.join(['0' if mark[i] == 1 else '1' for i in range(1, N+1)]))
    
    NA = collections.defaultdict(list)
    for u, vs in A.items():
        nvs = [v for v in vs if mark[v] == mark[u]]
        if nvs:
            NA[u] = nvs
    A = NA
    k += 1
    
    done = all(len(A[u]) == 0 for u in range(1, N+1))


if done:
    print(len(ans))
    print('\n'.join(ans))
else:
    print(-1)