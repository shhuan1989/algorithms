# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(H, C, T):
    if T >= H:
        return 1
    elif T <= (H+C)/2:
        return 2
    else:
        t = T - (H+C)/2
        # H/3, H/5, H/7, ..., close to t? == t
        h = int(H / t)
        d = t
        ans = 2
        
        def cal(a):
            return ((a+1)*H+a*C)/(2*a+1)
        
        lo, hi = 1, 10000
        while lo <= hi:
            if hi - lo <= 3:
                for i in range(lo, hi+1):
                    nd = abs(cal(i)-T)
                    if nd < d:
                        d = nd
                        ans = i
            
            m = (hi-lo) // 3
            a, b = lo + m, lo + m * 2
            avgl = abs(cal(lo)-T)
            avgr = abs(cal(hi)-T)
            avga = abs(cal(a)-T)
            avgb = abs(cal(b)-T)
            
            if avgl >= avga >= avgb:
                lo = b + 1
            elif avga <= avgb <= avgr:
                hi = a - 1
            else:
                lo, hi = a, b
        
        return 2 * ans  + 1

T = int(input())
ans = []
for ti in range(T):
    H, C, T = map(int, input().split())
    ans.append(solve(H, C, T))

print('\n'.join(map(str, ans)))