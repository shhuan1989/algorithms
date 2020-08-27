# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/11

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, K, F):
    wc = set()
    segs = 1
    for v in F:
        if v in wc:
            segs += 1
            wc = set()
        wc.add(v)
    
    if K == 1:
        return segs
    
    
    M = segs
    dp = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    
    for i in range(1, N+1):
        cost = 0
        wc = collections.defaultdict(int)
        for pi in range(i-1, -1, -1):
            f = F[pi]
            wc[f] += 1
            cost += 2 if wc[f] == 2 else (1 if wc[f] > 2 else 0)
            
            if cost == 0:
                if pi == 0:
                    dp[i][1] = K
                else:
                    nf = F[pi-1]
                    if wc[nf] == 0:
                        continue
            if cost > 2 * K:
                break
                
            for j in range(1, min(pi+1, M) + 1):
                dp[i][j] = min(dp[i][j], dp[pi][j-1] + cost + K)
    
    # print(dp[N])
    return min(dp[N])


if __name__ == '__main__':
    T = int(input())
    ans = []
    for _ in range(T):
        N, K = map(int, input().split())
        F = [int(x) for x in input().split()]
        ans.append(solve(N, K, F))
    
    print('\n'.join(map(str, ans)))