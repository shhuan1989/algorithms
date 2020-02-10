# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/15/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, A):
    pos = [i+M for i in range(N+1)]
    minpos = [i for i in range(N+1)]
    maxpos = [i for i in range(N+1)]
    
    bits = [0 for _ in range(N+M+1)]
    
    def add(index, val):
        while index <= N+M:
            bits[index] += val
            index |= index + 1
        
    def query(index):
        s = 0
        while index >= 0:
            s += bits[index]
            index = (index & (index + 1)) - 1
        
        return s
    
    for i in range(1, N + 1):
        add(i + M, 1)
        
    first = M
    for v in A:
        minpos[v] = 1
        maxpos[v] = max(maxpos[v], query(pos[v]-1) + 1)
        
        add(pos[v], -1)
        pos[v] = first
        first -= 1
        add(pos[v], 1)
        
    for v in range(1, N+1):
        maxpos[v] = max(maxpos[v], query(pos[v]-1) + 1)
    
    ans = ['{} {}'.format(a, b) for a, b in zip(minpos[1:], maxpos[1:])]
    print('\n'.join(ans))
        
    
N, M = map(int, input().split())
A = [int(x) for x in input().split()]
solve(N, M, A)