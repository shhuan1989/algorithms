# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/6

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


if __name__ == '__main__':
    N = int(input())
    A = [[] for _ in range(7)]
    
    for _ in range(N):
        p, t = map(int, input().split())
        A[p].append(t)
    
    ans = 0
    # for row in A:
    #     print(row)
    for i in range(7):
        A[i].sort()
        a = A[i]
        l, r = 0, 0
        while r < len(a):
            if a[r] - a[l] >= 60:
                ans += 1
                l = r
            r += 1
        if r > l:
            ans += 1
    
    print(ans)
    