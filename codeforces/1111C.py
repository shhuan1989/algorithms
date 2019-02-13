# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, K, A, B = map(int, input().split())
positions = [int(x) for x in input().split()]
positions.sort()


def count(l, r):
    a = bisect.bisect_left(positions, l)
    b = bisect.bisect_right(positions, r)
    return b-a
    

def solve(l, r):
    a, b = bisect.bisect_left(positions, l), bisect.bisect_right(positions, r)
    x = b - a
    ans = 0
    if x == 0:
        ans = A
    else:
        ans = B * x * (r-l+1)
    
    if l == r or x == 0:
        return ans
    
    m = (l+r) // 2
    ans = min(ans, solve(l, m) + solve(m+1, r))
    return ans


print(solve(1, 1 << N))
