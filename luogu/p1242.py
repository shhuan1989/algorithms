# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/31

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
    for i in range(3):
        row = [int(x) for x in input().strip().split()]
        v = 0
        for w in row[1:]:
            v |= 1 << w
        A.append(v)
    
    B = []
    for i in range(3):
        row = [int(x) for x in input().strip().split()]
        v = 0
        for w in row[1:]:
            v |= 1 << w
        B.append(v)
    
    
    def getmin(a):
        for i in range(1, 64):
            if a & (1 << i):
                return i
        return 0
    
    
    def move(a, b):
        s, t = getmin(a), getmin(b)
        if s <= 0:
            return False, s, a, b
        
        if 0 < t < s:
            return False, s, a, b
        
        a ^= 1 << s
        b |= 1 << s
        
        return True, s, a, b
    
    
    s, t = tuple(A), tuple(B)
    pre = {s: ('#', -1, -1, -1)}
    q = collections.deque([s])
    while q:
        u = q.popleft()
        if u == t:
            nq = []
            break
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                f, c, a, b = move(u[i], u[j])
                if not f:
                    continue
                v = [x for x in u]
                v[i] = a
                v[j] = b
                v = tuple(v)
                if v not in pre:
                    pre[v] = (u, c, i, j)
                    q.append(v)
    
    ans = []
    w = t
    name = ['A', 'B', 'C']
    while True:
        pw, v, i, j = pre[w]
        if pw == '#':
            break
        ans.append('move {} from {} to {}'.format(v, name[i], name[j]))
        w = pw
    print('\n'.join(reversed(ans)))
    print(len(ans))