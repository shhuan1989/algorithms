# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/17/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    wc = collections.Counter(A)
    vals = set(wc.keys())
    
    minv, maxv = min(vals), max(vals)
    ans = 0
    selected = []
    for v in vals:
        if wc[v] > ans:
            ans = wc[v]
            selected = [v]
        k = 1
        while v + k <= maxv:
            if v + k in vals:
                if v + k * 2 in vals:
                    count = wc[v] + wc[v+k] + wc[v+k*2]
                    if count > ans:
                        ans = count
                        selected = [v, v+k, v+k*2]
                else:
                    count = wc[v] + wc[v + k]
                    if count > ans:
                        ans = count
                        selected = [v, v + k]
            k *= 2
        
        k = 1
        while v-k >= minv:
            if v-k in vals:
                if v-k*2 in vals:
                    count = wc[v] + wc[v-k] + wc[v-k*2]
                    if count > ans:
                        ans = count
                        selected = [v, v-k, v-k*2]
                else:
                    count = wc[v] + wc[v-k]
                    if count > ans:
                        ans = count
                        selected = [v, v-k]
            k *= 2
    
    
    print(ans)
    print(' '.join([' '.join(map(str, [v] * wc[v])) for v in selected]))
    

N = int(input())
A = [int(x) for x in input().split()]
solve(N, A)