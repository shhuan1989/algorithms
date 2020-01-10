# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/9/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, P, T):
    dp = [[0 for _ in range(N+1)] for _ in range(T+1)]
    p = 1
    for t in range(T+1):
        dp[t][0] = p
        p *= (1 - P)
        
    for t in range(1, T+1):
        for i in range(1, min(N, t) + 1):
            dp[t][i] += dp[t-1][i-1] * P + dp[t-1][i] * (1-P if i < N else 1)
    
    # for row in dp:
    #     print(row)
    
    return sum([i * dp[T][i] for i in range(N+1)])
            

line = [x for x in input().split()]
N, P, T = int(line[0]), float(line[1]), int(line[2])
print(solve(N, P, T))