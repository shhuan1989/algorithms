# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('P1281_5.in', 'r')
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    INF = sum(A) + 1
    
    presum = [0]
    for v in A:
        presum.append(presum[-1] + v)
        
    dp = [[INF for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 0
    
    for i in range(1, N+1):
        for k in range(1, K+1):
            for pi in range(i):
                # cost = dp[pi][k-1] + sum(A[pi:i])
                cost = max(dp[pi][k-1], presum[i] - presum[pi])
                if cost < dp[i][k]:
                    dp[i][k] = cost

    ans = []
    t = 0
    cost = dp[N][K]
    r = N
    for i in range(N-1, -1, -1):
        if t + A[i] > cost:
            ans.append((i + 2, r))
            r = i + 1
            t = A[i]
        else:
            t += A[i]
    ans.append((1, r))
    print('\n'.join(['{} {}'.format(l, r) for l, r in ans[::-1]]))