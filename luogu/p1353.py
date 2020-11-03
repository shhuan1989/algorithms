# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0]
    for _ in range(N):
        A.append(int(input()))
    
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for i in range(1, N+1):
        dp[i][0] = max(dp[i-1][0], max(dp[i-j][j] for j in range(1, min(i, M)+1)))
        
        for j in range(1, min(M, i)+1):
            dp[i][j] = dp[i-1][j-1] + A[i]
            
    print(dp[N][0])
