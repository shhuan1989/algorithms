# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import lru_cache
if __name__ == '__main__':
    N, S = map(int, input().split())
    
    M = N * (N-1) // 2
    
    if abs(S) > M:
        print(0)
        exit(0)
        
    dp = [[[0 for _ in range(2 * M + 1)] for _ in range(2 * N + 1)] for _ in range(2)]
    dp[0][N][M] = 1
    for i in range(1, N):
        # ndp = [[0 for _ in range(2 * M + 1)] for _ in range(2 * N + 1)]
        for j in range(N-i, N+i+1):
            d = j - N
            s = i * (i+1) // 2
            for k in range(M-s, M+s+1):
                dp[i % 2][j][k] = dp[(i+1)%2][j+1][k-d] if j + 1 <= 2*N and 0 <= k-d <= 2*M else 0
                dp[i % 2][j][k] += dp[(i+1)%2][j-1][k-d] if j-1 >= 0 and 0 <= k-d <= 2*M else 0
    
    
    print(sum(dp[(N-1)%2][i][M+S] for i in range(2*N+1)))
    done = [0]
    ans = []
    def dfs(path, s, n):
        if done[0] >= 100:
            return
        if n >= N:
            if s == S:
                done[0] += 1
                if done[0] <= 100:
                    ans.append(' '.join(map(str, path)))
            return
        
        r = N-n
        maxr = r * (path[-1] + 1 + path[-1] + r) // 2
        minr = r * (path[-1]-1 + path[-1] - r) // 2
        d = S - s
        if d < minr or d > maxr:
            return
        
        dfs(path + [path[-1] - 1], s + path[-1] - 1, n+1)
        dfs(path + [path[-1] + 1], s + path[-1] + 1, n+1)
    
    
    dfs([0], 0, 1)
    # print(done[0])
    print('\n'.join(ans))
    