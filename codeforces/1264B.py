# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools


def place(a, b, c, d, av, bv, cv, dv):
    n = a + b + c + d
    s = [0 for _ in range(n)]
    
    i, w = 0, 0
    while w < a and i < n:
        s[i] = av
        i += 2
        w += 1
    
    j, w = 1, 0
    while w < b and j < n:
        s[j] = bv
        j += 2
        w += 1
        
    w = 0
    while w < c and i < n:
        s[i] = cv
        i += 2
    
    w = 0
    while w < d and j < n:
        s[j] = dv
        j += 2
        
    if s.count(av) == a and s.count(bv) == b and s.count(cv) == c and s.count(dv) == d and all([abs(s[i]-s[i+1]) == 1 for i in range(n-1)]):
        return s
        
    return []


def solve(a, b, c, d):
    for s in itertools.permutations([(a, 0), (b, 1), (c, 2), (d, 3)]):
        t = place(s[0][0], s[1][0], s[2][0], s[3][0], s[0][1], s[1][1], s[2][1], s[3][1])
        if t:
            print('YES')
            print(' '.join(map(str, t)))
            return
    print('NO')


a, b, c, d = map(int, input().split())
solve(a, b, c, d)