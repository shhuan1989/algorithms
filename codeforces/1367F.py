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


def solve(N, A):
    B = list(sorted(set(A)))
    A = [bisect.bisect_right(B, v-1) for v in A]
    
    dp = [1 for i in range(N+1)]
    vlast = [-1 for _ in range(N+1)]
    vfirst = [-1 for _ in range(N+1)]
    vcount = [0 for _ in range(N+1)]
    
    ans = 0
    for i, v in enumerate(A):
        
        a = max(dp[i], (dp[vfirst[v]] + vcount[v]) if vfirst[v] >= 0 else 0)
        b = (dp[vlast[v - 1]] if v - 1 >= 0 and vlast[v - 1] >= 0 else 0) + 1
        ans = max(ans, a, b)
        
        if vfirst[v] >= 0:
            dp[i] = max(dp[i], a)
        else:
            dp[i] = max(dp[i], b)
        
        vcount[v] += 1
        if vfirst[v] < 0:
            vfirst[v] = i
        vlast[v] = i
    print(A)
    print(dp)
    return N - ans
    

if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        ans.append(solve(N, A))
    
    print('\n'.join(map(str, ans)))


    