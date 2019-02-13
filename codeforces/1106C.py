# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/1/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N = int(input())
A = [int(x) for x in input().split()]

A.sort()

ans = 0
for i in range(N//2):
    ans += (A[i] + A[N-i-1]) ** 2
    
print(ans)
