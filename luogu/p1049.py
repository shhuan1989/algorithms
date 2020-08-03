# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    V = int(input())
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
        
    dp = [[0 for _ in range(V+1)] for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, V+1):
            dp[i][j] = dp[i-1][j]
            if j >= A[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-A[i-1]] + A[i-1])

    print(V - dp[N][V])