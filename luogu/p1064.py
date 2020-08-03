# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/10

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
    A = []
    G = collections.defaultdict(list)
    for i in range(1, M+1):
        v, w, p = map(int, input().split())
        if p == 0:
            G[i].append((1, v, w))
        else:
            G[p].append((2, v, w))
    
    for k, v in G.items():
        G[k].sort()
    
    roots = list(sorted(G.keys()))
    NG = len(roots)
    dp = [[0 for _ in range(N+1)] for _ in range(NG+1)]
    
    for gi in range(1, NG+1):
        for cap in range(N+1):
            group = G[roots[gi-1]]
            fo, fv, fw = group[0]
            
            # donot buy this group
            dp[gi][cap] = dp[gi-1][cap]

            # only buy main
            if cap >= fv:
                dp[gi][cap] = max(dp[gi][cap], dp[gi-1][cap-fv] + fv * fw)
            
            # buy main and one sub
            if len(group) > 1:
                for si in range(1, len(group)):
                    so, sv, sw = group[si]
                    if cap >= fv+sv:
                        dp[gi][cap] = max(dp[gi][cap], dp[gi-1][cap-fv-sv] + fv*fw + sv*sw)

            # buy two sub
            if len(group) > 2:
                av = sum([x[1] for x in group])
                aw = sum([x[1] * x[2] for x in group])
                if cap >= av:
                    dp[gi][cap] = max(dp[gi][cap], dp[gi-1][cap-av] + aw)
                    
    print(dp[NG][N])
            
            
            
            
            
            
            
    