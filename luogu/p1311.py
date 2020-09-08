# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, P, A, C):
    right = [N for _ in range(N)]
    for i in range(N - 1, -1, -1):
        if C[i] <= P:
            right[i] = i
        else:
            right[i] = right[i + 1] if i + 1 < N else N
    
    ans = 0
    # put presum in the loop will OOM
    presum = [0 for _ in range(N + 1)]
    for color in range(K):
        presum[0] = 0
        for i, c in enumerate(A):
            presum[i+1] = presum[i]
            if c == color:
                presum[i+1] += 1
        
        for i, c in enumerate(A):
            if c == color:
                r = max(right[i], i+1)
                ans += presum[N] - presum[r]
    print(ans)
    
    
    # presum = [[0 for _ in range(K)] for _ in range(N + 1)]
    # for i, c in enumerate(A):
    #     for j in range(K):
    #         presum[i + 1][j] = presum[i][j]
    #     presum[i + 1][c] += 1
    #
    # ans = 0
    # for i, c in enumerate(A):
    #     r = max(right[i], i + 1)
    #     ans += presum[N][c] - presum[r][c]
    #
    # print(ans)
    

if __name__ == '__main__':
    sys.stdin = open('P1311_2.in', 'r')
    N, K, P = map(int, input().strip().split())
    A, C = [], []
    for _ in range(N):
        a, c = map(int, input().split())
        A.append(a)
        C.append(c)
    
    solve(N, K, P, A, C)
