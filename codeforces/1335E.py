# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    uniq = list(sorted(set(A)))
    vmap = {v:i for i, v in enumerate(uniq)}
    A = [vmap[v] for v in A]
    
    wc = collections.Counter(A)
    ans = max(wc.values())
    
    M = len(uniq)
    K = ans
    pos = [[-1 for _ in range(K+1)] for _ in range(M)]
    left = [[0 for _ in range(N)] for _ in range(M)]
    
    cwc = collections.defaultdict(int)
    for i, v in enumerate(A):
        cwc[v] += 1
        pos[v][cwc[v]] = i
        
        if i > 0:
            for u in range(M):
                left[u][i] = left[u][i-1]
        left[v][i] += 1
        
    
    
    cwc = collections.defaultdict(int)
    for i, v in enumerate(A):
        cwc[v] += 1
        j = pos[v][wc[v]-cwc[v]+1] - 1
        if i < j:
            for u in range(M):
                ans = max(ans, cwc[v] * 2 + (left[u][j] - left[u][i]))
        
    return ans
    
    
    
    
    
    

if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        ans.append(solve(N, A))
    
    print('\n'.join(map(str, ans)))