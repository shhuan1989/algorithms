# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/21/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math


def solve(A, C, T):
    
    dp = {}
    
    dp[0] = {0: (0, set())}
    N = len(A)
    for k in range(1, N+1):
        dp[k] = {}
        for i, a in enumerate(A):
            m, s = a
            for x, vs in dp[k-1].items():
                prevm, previds = vs
            
                if (x+s not in dp[k] or prevm + m < dp[k][x+s][0]) and i not in previds:
                    dp[k][x+s] = (prevm + m, previds | {i})
    
    
    # print(A)
    ans = 0
    for k, v in dp.items():
        for score, midx in v.items():
            # print(k, v)
            m, idx = midx
            
            a = [(A[i][1]/A[i][0], A[i][0], A[i][1]) for i in idx]
            a.sort()
            a = [av[1] for av in a]
            
            # t = math.sqrt(m/C + 1/(4*C**2))-0.5/C
            # f = 10 * k + m / (1+C*t) + t
            # s = 1+C*t
            # f = 10*k + t + sigma(m/(s * 0.9**i))
            x = math.sqrt(C * sum([av/(0.9**(i+1)) for i, av in enumerate(a)]))
            t = (x-1)/C
            s = 1 + C*t
            f = 10*k + t + sum([av/(s * (0.9**(i+1))) for i, av in enumerate(a)])
            if f <= T:
                ans = max(ans, score)
    
    print(ans)



T = int(input())
for ti in range(T):
    N = int(input())
    C, T = map(float, input().split())
    A = []
    for i in range(N):
        a, p = map(int, input().split())
        A.append((a, p))
    
    solve(A, C, T)
        
        