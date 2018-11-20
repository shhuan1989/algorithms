# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/17/18

"""
# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/16 22:42

"""

N = int(input())

A = [int(x) for x in input().split()]


ans = 0
while True:
    updated = False
    wc = collections.defaultdict(int)
    for i in range(1, N-1):
        if updated:
            break
        if A[i] == 0 and A[i-1] == A[i+1] == 1:
            wc[i-1] += 1
            wc[i+1] += 1
            for v in [i-1, i+1]:
                if wc[v] > 1:
                    A[v] = 0
                    ans += 1
                    updated = True
                    break
                    
    # print(A)
    if not updated:
        break
        
for i in range(1, N-1):
    if A[i] == 0 and A[i-1] == A[i+1] == 1:
        A[i-1] = 0
        ans += 1
        
print(ans)
