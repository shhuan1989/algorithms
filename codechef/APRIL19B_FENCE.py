# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-04-07

"""

import collections
import time
import os
import sys
import bisect
import heapq

T = int(input())

for ti in range(T):
    N, M, K = map(int, input().split())
    plants = set()
    for ki in range(K):
        r, c = map(int, input().split())
        plants.add((r, c))
    
    vis = set()
    ans = 0
    for x in plants:
        if x in vis:
            continue
            
        q = [x]
        vis.add(x)
        while q:
            r, c = q.pop()
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                nrc = (nr, nc)
                if 1 <= nr <= N and 1 <= nc <= M:
                    if nrc in plants:
                        if nrc not in vis:
                            vis.add(nrc)
                            q.append(nrc)
                    else:
                        ans += 1
                else:
                    ans += 1
    print(ans)
    
    
    