# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    
    def getscore(mul):
        dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
        
        for i in range(N):
            dp[i][1] = A[i]

        for l in range(2, N+1):
            for i in range(N):
                if i + l > N:
                    continue
                for j in range(1, l):
                    if i+j-1 in mul:
                        dp[i][l] = max(dp[i][l], dp[i][j] * dp[i+j][l-j])
                    else:
                        dp[i][l] = max(dp[i][l], dp[i][j] + dp[i + j][l - j])
        
        return dp[0][N]
   
    ans = max(getscore(mul) for mul in itertools.combinations(range(N-1), K))
    # for mul in itertools.combinations(range(N-1), K):
    #     ans = max(ans, getscore(mul))
        
    print(ans)