# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('p1295.in', 'r')
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))
    
    # presum = [0]
    # for v in A:
    #     presum.append(presum[-1] + v)
    
    # rightmax = [0 for _ in range(N+1)]
    # l, r = 0, 0
    # s = 0
    # maxv = []
    # while r < N:
    #     if s + A[r] > M:
    #         while s + A[r] > M:
    #             while maxv and maxv[0][1] < l:
    #                 heapq.heappop(maxv)
    #             rightmax[l] = -maxv[0][0]
    #             s -= A[l]
    #             l += 1
    #         r -= 1
    #     else:
    #         s += A[r]
    #         heapq.heappush(maxv, (-A[r], r))
    #     r += 1
    #
    # while l < N:
    #     while maxv and maxv[0][1] < l:
    #         heapq.heappop(maxv)
    #     rightmax[l] = -maxv[0][0]
    #     l += 1
    #
    # print(rightmax)
    #
    
    # tree = [float('inf') for _ in range(N+1)]
    # def update(index, val):
    #     tree[index] = val
    #
    # def query(l, r):
    #     return min(tree[l: r+1])
    
    
    # def findpi(index):
    #     # presum[index] - presum[pi] > M
    #     lo, hi = 0, index
    #     while lo <= hi:
    #         pi = (lo + hi) // 2
    #         if presum[index] - presum[pi] <= M:
    #             hi = pi - 1
    #         else:
    #             lo = pi + 1
    #
    #     return lo
    
    # dp = [float('inf') for _ in range(N+1)]
    #
    # dp[0] = 0
    # q = []
    # for i in range(1, N+1):
    #     dp[i] = dp[i-1] + A[i-1]
    #
    #     v = A[i-1]
    #     while q and A[q[-1]-1] < v and presum[i]-presum[q[-1]-1] <= M:
    #         pi = q[-1]
    #         dp[i] = min(dp[i], v + query(pi, i-1))
    #         q.pop()
    #
    #     for pi in q[::-1]:
    #         if presum[i] - presum[pi-1] > M:
    #             break
    #         dp[i] = min(dp[i], A[pi-1] + dp[pi-1])
    #
    #     if presum[i] < M:
    #         dp[i] = min(dp[i], max(A[:i]))
    #
    #     q.append(i)
    #     update(i, dp[i])
        
        
        # s = A[i-1]
        # maxv = s
        # for pi in range(i-2, 0, -1):
        #     s += A[pi]
        #     maxv = max(maxv, A[pi])
        #     if s > M:
        #         break
        #     dp[i] = min(dp[i], dp[pi] + maxv)
    
    # print(dp)
    # print(dp[N])
    
            