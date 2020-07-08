# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/30

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, A):
    
    def check_impl(val, odd):
        s = 0 if odd else 1
        i = 0 if odd else 1
        while i < N:
            if A[i] <= val:
                s += 1
                if s >= K:
                    break
                if i + 1 < N:
                    s += 1
                i += 2
            else:
                i += 1
                
        return s >= K
        
    def check(val):
        return check_impl(val, True) or check_impl(val, False)
    
    lo, hi = 0, max(A)
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            hi = m - 1
        else:
            lo = m + 1
    
    return lo


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    print(solve(N, K, A))