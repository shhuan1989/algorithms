# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input()
    K += 1
    
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, min(K, i)+1):
            for pi in range(i):
                dp[i][j] = max(dp[i][j], dp[pi][j-1] * int(S[pi: i]))
    
    print(dp[N][K])