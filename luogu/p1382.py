# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/28

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    N = int(input())
    A = []
    H = set()
    X = set()
    for _ in range(N):
        h, l, r = map(int, input().strip().split())
        A.append((h, l, r))
        X.add(l)
        X.add(r)
        H.add(h)
    
    H.add(0)
    
    realh = list(sorted(H))
    normh = {h: i for i, h in enumerate(realh)}
    
    realx = list(sorted(X))
    normx = {x: i for i, x in enumerate(realx)}
    
    maxx = len(realx)
    add = [[] for _ in range(maxx)]
    remove = [[] for _ in range(maxx)]
    
    for h, l, r in A:
        h = normh[h]
        l = normx[l]
        r = normx[r]
        add[l].append(h)
        remove[r].append(h)
        X.add(l)
        X.add(r)
    
    ans = []
    
    
    def appendans(x, h):
        x = realx[x]
        h = realh[h]
        if not ans or ans[-1] != (x, h):
            ans.append((x, h))
    
    
    q = []
    maxh = len(realh)
    removed = [0 for _ in range(maxh)]
    preh = 0
    prex = float('inf')
    for x in range(maxx):
        for h in add[x]:
            heapq.heappush(q, -h)
        
        for h in remove[x]:
            removed[h] += 1
        
        h = abs(q[0])
        while removed[h] > 0:
            heapq.heappop(q)
            removed[h] -= 1
            
            if not q:
                h = -0
                break
            h = abs(q[0])
        
        if h != preh:
            if prex != float('inf'):
                appendans(prex, preh)
                appendans(x, preh)
                appendans(x, h)
            else:
                appendans(x, 0)
                appendans(x, h)
            preh = h
            prex = x if h > 0 else float('inf')
    
    print(len(ans))
    print('\n'.join(['{} {}'.format(x, h) for x, h in ans]))
