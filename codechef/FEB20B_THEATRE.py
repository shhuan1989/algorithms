# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools


def solve(N, A):
    
    wc = collections.defaultdict(int)
    for m, t in A:
        wc[m, t] += 1
    
    ans = float('-inf')
    for movie in itertools.permutations(['A', 'B', 'C', 'D']):
        for ticket in itertools.permutations([25, 50, 75, 100]):
            revenue = 0
            
            for m, t, p in zip(movie, [12, 3, 6, 9], ticket):
                c = wc[m, t]
                if c == 0:
                    revenue -= 100
                else:
                    revenue += c * p
            ans = max(ans, revenue)
    
    return ans


T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = []
    for i in range(N):
        m, t = input().split()
        A.append((m, int(t)))
    ans.append(solve(N, A))
    
print('\n'.join(map(str, ans)))
print(sum(ans))