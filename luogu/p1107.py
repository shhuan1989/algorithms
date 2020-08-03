# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    N, H, D = map(int, input().split())
    S = [[0 for _ in range(N)] for _ in range(H + 1)]
    vh = set()
    for i in range(N):
        hs = [int(x) for x in input().split()]
        for h in hs:
            if h > H:
                continue
            S[h][i] += 1
            vh.add(h)
    
    vh.add(0)
    VH = list(sorted(vh, reverse=True))
    PREH = [h + 1 for h in range(H + 1)]
    for vi in range(1, len(VH)):
        PREH[VH[vi]] = VH[vi - 1]
    
    # for h in range(H, -1, -1):
    #     print(S[h])
    dp = [[0 for _ in range(N)] for _ in range(H + 1)]
    dph = [0 for _ in range(H + 1)]
    for i in range(N):
        dp[H][i] = S[H][i]
    dph[H] = max(dp[H])
    for h in VH[1:]:
        for i in range(N):
            dp[h][i] = max(dp[h][i], dp[PREH[h]][i] + S[h][i])
            if h + D <= H:
                dp[h][i] = max(dp[h][i], S[h][i] + dph[h + D])
        
        dph[h] = max(dp[h])
    
    # print(dph)
    
    print(dph[0])




