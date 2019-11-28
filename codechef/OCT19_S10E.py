# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/9/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


T = int(input())
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    
    ans = 0
    for i, a in enumerate(A):
        if a < min(A[max(i-5, 0): i] or [float('inf')]):
            ans += 1
            
    print(ans)