# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/3/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, X, S):
    si = {}
    ss = list(sorted(set(S)))
    for i, s in enumerate(ss):
        si[s] = i
        
    xs = [(x, si[s]) for x, s in zip(X, S)]
    xs.sort()
    
    
    bitc = [0 for _ in range(N+1)]
    bitx = [0 for _ in range(N+1)]
    
    def add(index, val):
        while index <= N:
            bitc[index] += 1
            bitx[index] += val
            index |= index + 1
    
    def get(index):
        count, xsum = 0, 0
        while index >= 0:
            count += bitc[index]
            xsum += bitx[index]
            index = (index & (index + 1)) - 1
            
        return count, xsum
        
    ans = 0
    for x, s in xs:
        count, xsum = get(s)
        ans += count * x - xsum
        add(s, x)
    
    return ans
    

N = int(input())
X = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]
print(solve(N, X, S))
