# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache
sys.setrecursionlimit(2000)

if __name__ == '__main__':
    # sys.stdin = open('P1280_10.in', 'r')
    N, K = map(int, input().split())
    work = []
    for i in range(K):
        s, t = map(int, input().split())
        work.append((s, s + t - 1))
    
    work.sort()
    
    @lru_cache(maxsize=None)
    def dfs(index):
        if index >= K:
            return 0
        
        end = work[index][1]
        l = bisect.bisect_right(work, (end, float('inf')))
        if l >= K:
            return N - end
        r = bisect.bisect_right(work, (work[l][0], float('inf')))
        ans = 0
        for i in range(l, r):
            ans = max(ans, work[i][0] - end - 1 + dfs(i))
        
        return ans
    
    ans = 0
    for i in range(K):
        if work[i][0] == work[0][0]:
            ans = max(ans, dfs(i) + work[0][0] - 1)
        else:
            break
    print(ans)
        
    
    
    
    
    
        